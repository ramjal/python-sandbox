import sys
print(sys.path)
sys.path.append(r"C:\DevLcl\Sandbox\Python")
print(sys.path)
import testing_import_source
print('')
print('*** runnint the test ***')
print('')
testing_import_source.test_import()
testing_import_source.test_multi(3, 5)
testing_import_source.test_multi(15, 54)
