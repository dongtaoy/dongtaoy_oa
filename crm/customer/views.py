from django.shortcuts import render, redirect
from crm.models import Customer
from crm.models import CustomerType
from system.models import Permission
from django.template import RequestContext
from collections import defaultdict
from hashlib import md5

