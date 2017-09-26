import io
import re
from omsdk.sdkprint import PrettyPrint
from omsdk.typemgr.FieldType import FieldType
from omsdk.typemgr.ClassType import ClassType
from omsdk.typemgr.BuiltinTypes import RootClassType
from omsdk.typemgr.ArrayType import ArrayType
from omsdk.sdkcenum import TypeHelper

class FormatterTemplate(object):
    def __init__(self, everything):
        self.everything = everything
        self.include_composite = True
        self.target = None

    def _emit(self, output, value):
        return 0

    def _init(self, output, obj, space, array=False):
        return None

    def _close(self, output, obj, space):
        pass

    def _write(self, output, attr_name, value, space):
        pass

    def _get_str(self):
        return None

    def format_type(self, obj):
        if obj:
            self._format_recurse(self.target, obj, space='')
        return self

    def _format_recurse(self, output_obj, obj, space):
        if isinstance(obj, FieldType):
            return self._emit(output_obj, obj)
        opobj = self._init(output_obj, obj, space, isinstance(obj, ArrayType))
        props = obj.Properties
        for i in props:
            if isinstance(i, str):
                if not self.everything:
                    if not obj.__dict__[i].is_changed():
                        continue
                if obj.__dict__[i]._composite and \
                   not self.include_composite:
                    continue
                attr_name = i
                if obj.__dict__[i]._alias is not None:
                    attr_name = obj.__dict__[i]._alias
                attr_name = re.sub('_.*', '', attr_name)
                if obj._fname is None:
                    attr_name = obj._alias + "." + str(obj.__dict__[i]._index) + "#" + attr_name
                self._write(opobj, attr_name, obj.__dict__[i], space)
            else:
                if not self.everything and not i.is_changed():
                    continue
                entry = self._create_array_entry(opobj)
                entry = self._format_recurse(entry, i, space + '  ')
                entry = self._close_array_entry(opobj, entry)
        self._close(opobj, obj, space)
        return opobj

    def printx(self):
        print(self._get_str())

class JSONFormatter(FormatterTemplate):
    def __init__(self, everything):
        super().__init__(everything)
        self.target = {}

    def _emit(self, output, value):
        return value

    def _init(self, output, obj, space, array=False):
        data = {}
        if array: data = []
        if obj._fname:
            output[obj._fname] = data
            return output[obj._fname]
        elif obj._alias and isinstance(obj, ClassType):
            output[obj._alias] = data
            return output[obj._alias]
        return output

    def _create_array_entry(self, opobj):
        return {}

    def _close_array_entry(self, opobj, obj):
        opobj.append(obj)
        return {}

    def _write(self, output, attr_name, value, space):
        output[attr_name] = self._format_recurse(output, value, space)

    def _get_str(self):
        return PrettyPrint.prettify_json(self.target)

class XMLFormatter(FormatterTemplate):
    def __init__(self, everything):
        super().__init__(everything)
        self.target = io.StringIO()
        self.include_composite = False

    def _emit(self, output, value):
        val = value.sanitized_value()
        if val: output.write(str(val))
        return 0

    def _init(self, output, obj, space, array=False):
        if obj._fname and not array:
            output.write(space + '<{0}'.format(obj._fname))
            for i in obj._attribs:
                output.write(' {0}="{1}"'.format(i, obj._attribs[i])) 
            output.write('>\n') 
        return output

    def _close(self, output, obj, space):
        if obj._fname:
            output.write(space +'</{0}>\n'.format(obj._fname))

    def _create_array_entry(self, output):
        return output

    def _close_array_entry(self, opobj, obj):
        return 

    def _write(self, output, attr_name, value, space):
        if value._fname:
            output.write(space+'<{0} name="{1}">'.  format(value._fname, attr_name))
            if not isinstance(value, FieldType):
                output.write('\n')
        self._format_recurse(output, value, space + '  ')
        if value._fname:
            output.write('</{0}>\n'.format(value._fname))

    def _get_str(self):
        return self.target.getvalue()

class StringFormatter(FormatterTemplate):
    def __init__(self, everything):
        super().__init__(everything)
        self.target = io.StringIO()

    def _emit(self, output, value):
        val = value.sanitized_value()
        if val: output.write(str(val))
        return 0

    def _init(self, output, obj, space):
        if obj._fname:
            output.write('{0}=['.format(obj._fname))
        return output

    def _close(self, output, obj):
        if obj._fname:
            output.write(']\n'.format(obj._fname))

    def _write(self, output, attr_name, value, space):
        if value._fname:
            output.write('{1}='.  format(value._fname, attr_name))
        self._format_recurse(output, value)
        if value._fname:
            output.write(','.format(value._fname))

    def _get_str(self):
        return self.target.getvalue()
