#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.3),
    on October 11, 2022, at 17:41
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

from pylsl import StreamInfo, StreamOutlet

info = StreamInfo('GraspMarkerStream', 'Markers', 1, 0, 'string', 'myuidw43536')

# next make an outlet
outlet = StreamOutlet(info)

print("sending grasp markers...")

outlet.push_sample(["ExptBeg"])


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.3'
expName = 'hand-grasp-v2'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001', 'group': ['A', 'B', 'C', 'D', 'E', 'F']}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='E:\\studies\\college\\IIT Gandhinagar\\SEM III\\CG 599 Thesis\\Grasp Experiment\\hand-grasp-v2_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "Welcome"
WelcomeClock = core.Clock()
WelcomeScr = visual.TextStim(win=win, name='WelcomeScr',
    text='Welcome to the experiment. \n\nRead the instructions on the next screen carefully.\n\nYou can choose to quit the study at any point during the experiment by informing the experimenter.\n\nPress SPACE to continue.\n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()
counterbalance = 'palmPos' + str(expInfo['group']) + ".csv"


# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
InstructionsScr = visual.TextStim(win=win, name='InstructionsScr',
    text="Your task is to open and close your palms (as shown by the experimenter).\n\nYou will begin by closing your palms. There are three blocks with three different positions of the arms. You will begin by closing your palms in the orientation as indicated.\n\nRemember to only move your palms when instructed and not any other part of your body. \n\nYou will also get breaks in between, you may stretch in that time only.\n\nPress SPACE when you're ready!\n\n\n",
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "Position"
PositionClock = core.Clock()
PositionMsg = visual.TextStim(win=win, name='PositionMsg',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Fixation"
FixationClock = core.Clock()
FixScr = visual.TextStim(win=win, name='FixScr',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "FistAction"
FistActionClock = core.Clock()
FistActionScr = visual.TextStim(win=win, name='FistActionScr',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Break"
BreakClock = core.Clock()
BreakScr = visual.TextStim(win=win, name='BreakScr',
    text='Please take a 1 minute break (minimum).\n\nPress SPACE when you are ready to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "FreeHandInst"
FreeHandInstClock = core.Clock()
FreeHandInsst = visual.TextStim(win=win, name='FreeHandInsst',
    text='In this final task, you have to open and close your palms in any position (from 3 before) in any manner you wish.\n\nWhen you see the plus sign, decide what hand to open/close and the position.\n\nWhen you see GO, then you perform the action. Press SPACE to continue.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "FreeFix"
FreeFixClock = core.Clock()
FreeFixScr = visual.TextStim(win=win, name='FreeFixScr',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "FreeFistAct"
FreeFistActClock = core.Clock()
FreeFistActScr = visual.TextStim(win=win, name='FreeFistActScr',
    text='GO',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Thank_you"
Thank_youClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Thank you for participating in the experiment.\n\nThe experiment will end now...',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Welcome"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
WelcomeComponents = [WelcomeScr, key_resp_2]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WelcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Welcome"-------
while continueRoutine:
    # get current time
    t = WelcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WelcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *WelcomeScr* updates
    if WelcomeScr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        WelcomeScr.frameNStart = frameN  # exact frame index
        WelcomeScr.tStart = t  # local t and not account for scr refresh
        WelcomeScr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(WelcomeScr, 'tStartRefresh')  # time at next scr refresh
        WelcomeScr.setAutoDraw(True)
    if WelcomeScr.status == STARTED:
        if bool(0):
            # keep track of stop time/frame for later
            WelcomeScr.tStop = t  # not accounting for scr refresh
            WelcomeScr.frameNStop = frameN  # exact frame index
            win.timeOnFlip(WelcomeScr, 'tStopRefresh')  # time at next scr refresh
            WelcomeScr.setAutoDraw(False)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Welcome"-------
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('WelcomeScr.started', WelcomeScr.tStartRefresh)
thisExp.addData('WelcomeScr.stopped', WelcomeScr.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
InstructionsComponents = [InstructionsScr, key_resp]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InstructionsScr* updates
    if InstructionsScr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        InstructionsScr.frameNStart = frameN  # exact frame index
        InstructionsScr.tStart = t  # local t and not account for scr refresh
        InstructionsScr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(InstructionsScr, 'tStartRefresh')  # time at next scr refresh
        InstructionsScr.setAutoDraw(True)
    if InstructionsScr.status == STARTED:
        if bool(0):
            # keep track of stop time/frame for later
            InstructionsScr.tStop = t  # not accounting for scr refresh
            InstructionsScr.frameNStop = frameN  # exact frame index
            win.timeOnFlip(InstructionsScr, 'tStopRefresh')  # time at next scr refresh
            InstructionsScr.setAutoDraw(False)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('InstructionsScr.started', InstructionsScr.tStartRefresh)
thisExp.addData('InstructionsScr.stopped', InstructionsScr.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
positionBlock = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(counterbalance),
    seed=None, name='positionBlock')
thisExp.addLoop(positionBlock)  # add the loop to the experiment
thisPositionBlock = positionBlock.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPositionBlock.rgb)
if thisPositionBlock != None:
    for paramName in thisPositionBlock:
        exec('{} = thisPositionBlock[paramName]'.format(paramName))

for thisPositionBlock in positionBlock:
    currentLoop = positionBlock
    # abbreviate parameter names if possible (e.g. rgb = thisPositionBlock.rgb)
    if thisPositionBlock != None:
        for paramName in thisPositionBlock:
            exec('{} = thisPositionBlock[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Position"-------
    continueRoutine = True
    routineTimer.add(4.000000)
    # update component parameters for each repeat
    PositionMsg.setText(condMessage)
    # keep track of which components have finished
    PositionComponents = [PositionMsg]
    for thisComponent in PositionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PositionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Position"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = PositionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PositionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *PositionMsg* updates
        if PositionMsg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            PositionMsg.frameNStart = frameN  # exact frame index
            PositionMsg.tStart = t  # local t and not account for scr refresh
            PositionMsg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(PositionMsg, 'tStartRefresh')  # time at next scr refresh
            PositionMsg.setAutoDraw(True)
        if PositionMsg.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > PositionMsg.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                PositionMsg.tStop = t  # not accounting for scr refresh
                PositionMsg.frameNStop = frameN  # exact frame index
                win.timeOnFlip(PositionMsg, 'tStopRefresh')  # time at next scr refresh
                PositionMsg.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PositionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Position"-------
    for thisComponent in PositionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    positionBlock.addData('PositionMsg.started', PositionMsg.tStartRefresh)
    positionBlock.addData('PositionMsg.stopped', PositionMsg.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(condsFile),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Fixation"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        outlet.push_sample(["FixBeg-" + condsFile[5:-4] + "-" + Hand + "-" + Action])
        # keep track of which components have finished
        FixationComponents = [FixScr]
        for thisComponent in FixationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        FixationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Fixation"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = FixationClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=FixationClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *FixScr* updates
            if FixScr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FixScr.frameNStart = frameN  # exact frame index
                FixScr.tStart = t  # local t and not account for scr refresh
                FixScr.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FixScr, 'tStartRefresh')  # time at next scr refresh
                FixScr.setAutoDraw(True)
            if FixScr.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > FixScr.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    FixScr.tStop = t  # not accounting for scr refresh
                    FixScr.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(FixScr, 'tStopRefresh')  # time at next scr refresh
                    FixScr.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FixationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Fixation"-------
        for thisComponent in FixationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('FixScr.started', FixScr.tStartRefresh)
        trials.addData('FixScr.stopped', FixScr.tStopRefresh)
        outlet.push_sample(["FixEnd-" + condsFile[5:-4] + "-" + Hand + "-" + Action])
        
        # ------Prepare to start Routine "FistAction"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        FistActionScr.setText(Action
)
        outlet.push_sample(["ActionBeg-" + condsFile[5:-4] + "-" + Hand + "-" + Action])
        # keep track of which components have finished
        FistActionComponents = [FistActionScr]
        for thisComponent in FistActionComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        FistActionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "FistAction"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = FistActionClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=FistActionClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *FistActionScr* updates
            if FistActionScr.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                FistActionScr.frameNStart = frameN  # exact frame index
                FistActionScr.tStart = t  # local t and not account for scr refresh
                FistActionScr.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FistActionScr, 'tStartRefresh')  # time at next scr refresh
                FistActionScr.setAutoDraw(True)
            if FistActionScr.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > FistActionScr.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    FistActionScr.tStop = t  # not accounting for scr refresh
                    FistActionScr.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(FistActionScr, 'tStopRefresh')  # time at next scr refresh
                    FistActionScr.setAutoDraw(False)
            rect_hand = visual.Rect(
                win, 
                size=(0.3, 0.2), 
                fillColor="white",
                units="norm"
            )
            FistActionScr.alignText = "center"
            if Hand == "Left":
                rect_hand.pos = (-0.5, 0)
                FistActionScr.pos = (-0.45, 0)
            elif Hand == "Right":
                rect_hand.pos = (0.5, 0)
                FistActionScr.pos = (0.45, 0)
            rect_hand.draw()
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FistActionComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "FistAction"-------
        for thisComponent in FistActionComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        outlet.push_sample(["ActionEnd-" + condsFile[5:-4] + "-" + Hand + "-" + Action])
    # completed 1.0 repeats of 'trials'
    
    
    # ------Prepare to start Routine "Break"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    BreakComponents = [BreakScr, key_resp_4]
    for thisComponent in BreakComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    BreakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Break"-------
    while continueRoutine:
        # get current time
        t = BreakClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=BreakClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *BreakScr* updates
        if BreakScr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            BreakScr.frameNStart = frameN  # exact frame index
            BreakScr.tStart = t  # local t and not account for scr refresh
            BreakScr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(BreakScr, 'tStartRefresh')  # time at next scr refresh
            BreakScr.setAutoDraw(True)
        if BreakScr.status == STARTED:
            if bool(0):
                # keep track of stop time/frame for later
                BreakScr.tStop = t  # not accounting for scr refresh
                BreakScr.frameNStop = frameN  # exact frame index
                win.timeOnFlip(BreakScr, 'tStopRefresh')  # time at next scr refresh
                BreakScr.setAutoDraw(False)
        
        # *key_resp_4* updates
        waitOnFlip = False
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 60-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BreakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Break"-------
    for thisComponent in BreakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    positionBlock.addData('BreakScr.started', BreakScr.tStartRefresh)
    positionBlock.addData('BreakScr.stopped', BreakScr.tStopRefresh)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    positionBlock.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        positionBlock.addData('key_resp_4.rt', key_resp_4.rt)
    positionBlock.addData('key_resp_4.started', key_resp_4.tStartRefresh)
    positionBlock.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
    # the Routine "Break" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'positionBlock'


# ------Prepare to start Routine "FreeHandInst"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
FreeHandInstComponents = [FreeHandInsst, key_resp_3]
for thisComponent in FreeHandInstComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
FreeHandInstClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "FreeHandInst"-------
while continueRoutine:
    # get current time
    t = FreeHandInstClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=FreeHandInstClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *FreeHandInsst* updates
    if FreeHandInsst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        FreeHandInsst.frameNStart = frameN  # exact frame index
        FreeHandInsst.tStart = t  # local t and not account for scr refresh
        FreeHandInsst.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(FreeHandInsst, 'tStartRefresh')  # time at next scr refresh
        FreeHandInsst.setAutoDraw(True)
    if FreeHandInsst.status == STARTED:
        if bool(0):
            # keep track of stop time/frame for later
            FreeHandInsst.tStop = t  # not accounting for scr refresh
            FreeHandInsst.frameNStop = frameN  # exact frame index
            win.timeOnFlip(FreeHandInsst, 'tStopRefresh')  # time at next scr refresh
            FreeHandInsst.setAutoDraw(False)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FreeHandInstComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "FreeHandInst"-------
for thisComponent in FreeHandInstComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('FreeHandInsst.started', FreeHandInsst.tStartRefresh)
thisExp.addData('FreeHandInsst.stopped', FreeHandInsst.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "FreeHandInst" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
FreeHandTrials = data.TrialHandler(nReps=40.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='FreeHandTrials')
thisExp.addLoop(FreeHandTrials)  # add the loop to the experiment
thisFreeHandTrial = FreeHandTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisFreeHandTrial.rgb)
if thisFreeHandTrial != None:
    for paramName in thisFreeHandTrial:
        exec('{} = thisFreeHandTrial[paramName]'.format(paramName))

for thisFreeHandTrial in FreeHandTrials:
    currentLoop = FreeHandTrials
    # abbreviate parameter names if possible (e.g. rgb = thisFreeHandTrial.rgb)
    if thisFreeHandTrial != None:
        for paramName in thisFreeHandTrial:
            exec('{} = thisFreeHandTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "FreeFix"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    outlet.push_sample(["FreeFixBeg"])
    # keep track of which components have finished
    FreeFixComponents = [FreeFixScr]
    for thisComponent in FreeFixComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FreeFixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "FreeFix"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FreeFixClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FreeFixClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FreeFixScr* updates
        if FreeFixScr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FreeFixScr.frameNStart = frameN  # exact frame index
            FreeFixScr.tStart = t  # local t and not account for scr refresh
            FreeFixScr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FreeFixScr, 'tStartRefresh')  # time at next scr refresh
            FreeFixScr.setAutoDraw(True)
        if FreeFixScr.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FreeFixScr.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                FreeFixScr.tStop = t  # not accounting for scr refresh
                FreeFixScr.frameNStop = frameN  # exact frame index
                win.timeOnFlip(FreeFixScr, 'tStopRefresh')  # time at next scr refresh
                FreeFixScr.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FreeFixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "FreeFix"-------
    for thisComponent in FreeFixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    FreeHandTrials.addData('FreeFixScr.started', FreeFixScr.tStartRefresh)
    FreeHandTrials.addData('FreeFixScr.stopped', FreeFixScr.tStopRefresh)
    outlet.push_sample(["FreeFixEnd"])
    
    # ------Prepare to start Routine "FreeFistAct"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    outlet.push_sample(["FreeHandBeg"])
    # keep track of which components have finished
    FreeFistActComponents = [FreeFistActScr]
    for thisComponent in FreeFistActComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FreeFistActClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "FreeFistAct"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FreeFistActClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FreeFistActClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FreeFistActScr* updates
        if FreeFistActScr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FreeFistActScr.frameNStart = frameN  # exact frame index
            FreeFistActScr.tStart = t  # local t and not account for scr refresh
            FreeFistActScr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FreeFistActScr, 'tStartRefresh')  # time at next scr refresh
            FreeFistActScr.setAutoDraw(True)
        if FreeFistActScr.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FreeFistActScr.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                FreeFistActScr.tStop = t  # not accounting for scr refresh
                FreeFistActScr.frameNStop = frameN  # exact frame index
                win.timeOnFlip(FreeFistActScr, 'tStopRefresh')  # time at next scr refresh
                FreeFistActScr.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FreeFistActComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "FreeFistAct"-------
    for thisComponent in FreeFistActComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    FreeHandTrials.addData('FreeFistActScr.started', FreeFistActScr.tStartRefresh)
    FreeHandTrials.addData('FreeFistActScr.stopped', FreeFistActScr.tStopRefresh)
    outlet.push_sample(["FreeHandEnd"])
    thisExp.nextEntry()
    
# completed 40.0 repeats of 'FreeHandTrials'


# ------Prepare to start Routine "Thank_you"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
Thank_youComponents = [text_2]
for thisComponent in Thank_youComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Thank_youClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Thank_you"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = Thank_youClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Thank_youClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    if text_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_2.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            text_2.tStop = t  # not accounting for scr refresh
            text_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStopRefresh')  # time at next scr refresh
            text_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Thank_youComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Thank_you"-------
for thisComponent in Thank_youComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
outlet.push_sample(["ExptEnd"])
outlet.push_sample(["ExptEnd"])

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
