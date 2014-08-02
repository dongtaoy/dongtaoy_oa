from django.shortcuts import render, redirect
from hr.models import User
from system.models import Permission
from django.template import RequestContext
from collections import defaultdict
from hashlib import md5

