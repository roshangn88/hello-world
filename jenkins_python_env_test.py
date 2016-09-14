import sys
import os

print "AWS_INSTANCE_TYPE :: %s"%os.environ["AWS_INSTANCE_TYPE"]
print "AWS_HOSTNAME :: %s"%os.environ["AWS_HOSTNAME"]
print "SERVER IP :: %s"%os.environ["SERVER"]
