import subprocess
import sys
import os
from pathlib import Path

import __main__
from behave import *

args = []


@given("Server Address '{ADDR}'")
def step_impl(context, ADDR):
    context.addr = str(ADDR)
    args.append("-a")
    args.append(str(ADDR))


@given("Server port '{PORT}'")
def step_impl(context, PORT):
    context.port = str(PORT)
    args.append("-p")
    args.append(str(PORT))


@given("Output file '{PATH}'")
def step_impl(context, PATH):
    context.PATH = PATH
    args.append("-o")
    args.append(str(PATH))



@when(u'Client Starts')
def step_impl(context):
    lstr = "python __main__.py -a " + context.addr + " -p " + context.port + " -o \""+ context.PATH + "\""
    try:
        context.proc = subprocess.Popen(lstr, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, universal_newlines=True)
        context.lines = []
        for line in context.proc.stdout:
            context.lines.append(line)
        context.proc.wait()
    except Exception as e:
        context.ex = e

@when(u'Client Starts without args')
def step_impl(context):
    lstr = "python __main__.py"
    try:
        context.proc = subprocess.Popen(lstr, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, universal_newlines=True)
        context.lines = []
        for line in context.proc.stdout:
            context.lines.append(line)
        context.proc.wait()
    except Exception as e:
        context.ex = e

@then("Output file should contain some text")
def step_impl(context):
    with open(context.PATH, "r") as f:
        lines = f.readlines()
        for line in lines:
            text = line.split("-")[0]
            assert text == "2018"


@then("[WinError {ERRCODE}]")
def step_impl(context, ERRCODE):
    tmp = context.lines.pop()
    t = tmp.split(' ')[1][:-1]
    print("" + str(t))
    assert str(ERRCODE) == str(t), tmp

@then(u'Help message is displayed')
def step_impl(context):
    tmp = context.lines.pop(0)
    t = tmp.split(' ')[0][:-1]
    assert "usage" == t, context.lines.pop()

