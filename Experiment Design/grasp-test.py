#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.3),
    on August 30, 2022, at 13:10
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



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.3'
expName = 'grasp-test'  # from the Builder filename that created this script
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
    originPath='E:\\studies\\college\\IIT Gandhinagar\\SEM III\\CG 599 Thesis\\Grasp Experiment\\grasp-test.py',
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
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
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

# Initialize components for Routine "Position"
PositionClock = core.Clock()
PositionMsg = visual.TextStim(win=win, name='PositionMsg',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
counterbalance = 'palmPos' + str(expInfo['group']) + ".csv"
print(counterbalance)

# Initialize components for Routine "Fixation"
FixationClock = core.Clock()
FixationScr = visual.TextStim(win=win, name='FixationScr',
    text='',
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
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
rect = visual.rect(
    win, 
    size=(1, 1), 
    fillColor="white",
    units="norm"
)
if Hand == "Left":
    rect.setPos(-0.5, 0)
elif Hand == "Right":
    rect.setPos(0.5, 0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

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
    routineTimer.add(5.000000)
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
            if tThisFlipGlobal > PositionMsg.tStartRefresh + 5-frameTolerance:
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
        FixationScr.setText(Hand
)
        # keep track of which components have finished
        FixationComponents = [FixationScr]
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
            
            # *FixationScr* updates
            if FixationScr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FixationScr.frameNStart = frameN  # exact frame index
                FixationScr.tStart = t  # local t and not account for scr refresh
                FixationScr.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FixationScr, 'tStartRefresh')  # time at next scr refresh
                FixationScr.setAutoDraw(True)
            if FixationScr.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > FixationScr.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    FixationScr.tStop = t  # not accounting for scr refresh
                    FixationScr.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(FixationScr, 'tStopRefresh')  # time at next scr refresh
                    FixationScr.setAutoDraw(False)
            
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
        trials.addData('FixationScr.started', FixationScr.tStartRefresh)
        trials.addData('FixationScr.stopped', FixationScr.tStopRefresh)
        
        # ------Prepare to start Routine "FistAction"-------
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        FistActionScr.setText(Action
)
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
            if FistActionScr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
        trials.addData('FistActionScr.started', FistActionScr.tStartRefresh)
        trials.addData('FistActionScr.stopped', FistActionScr.tStopRefresh)
    # completed 1.0 repeats of 'trials'
    
# completed 1.0 repeats of 'positionBlock'


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
