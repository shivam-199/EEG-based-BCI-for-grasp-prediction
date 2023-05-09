fileList=dir('Raw/*.xdf');
for i=1:size(fileList)
    %% Reading files, adding channel location, filter, resampling, clean artifact, interpolation, rereferencing
    fileName=fileList(i).name;
    EEG = pop_loadxdf(strcat(fileList(i).folder, "/", fileName));
    chanLoc = readlocs('/mnt/sda1/shivam/Thesis/Grasp Experiment/Data/ChannelLocations/EGIAmpServer64Chan.loc');
    EEG.chanlocs = chanLoc;
    
    %EEG = pop_resample(EEG, 250);
    
    EEG = pop_eegfiltnew(EEG, [], 40, [], false, [], 0);
    EEG = pop_eegfiltnew(EEG, 1, [], [], false, [], 0);
    
    originalEEG = EEG;
    
    originalEEG = pop_runica(originalEEG, 'icatype', 'runica');
    
    originalEEG.icaact = (originalEEG.icaweights * originalEEG.icasphere) * originalEEG.data;
    
    %EEGc=clean_artifacts(originalEEG);
    %EEGin = pop_interp(EEGc, originalEEG.chanlocs, 'spherical');
    %EEGref = pop_reref( EEGin, []);
    
    % Baseline correction
    %EEGbc = pop_rmbase()
    
    EEG = pop_saveset(originalEEG, 'filename', fileName(1:end-4), 'filepath', '/mnt/sda1/shivam/Thesis/Grasp Experiment/Data/PreprocessedData/ICs');
    
    %%
    %save(['Preprocessedv4/cf_',fileName(1:end-3),'mat'],'EEG*');
    %{
    %% Renaming event markers
    
    EEGstimDRO = pop_epoch( EEGref, {'ActionBeg-palmDown-Right-Open'}, [-0.1 1],'newname', 'StimDRO','epochinfo','yes');
    EEGstimDRC = pop_epoch( EEGref, {'ActionBeg-palmDown-Right-Close'}, [-0.1 1],'newname', 'StimDRC','epochinfo','yes');
    EEGstimDLO = pop_epoch( EEGref, {'ActionBeg-palmDown-Left-Open'}, [-0.1 1],'newname', 'StimDLO','epochinfo','yes');
    EEGstimDLC = pop_epoch( EEGref, {'ActionBeg-palmDown-Left-Close'}, [-0.1 1],'newname', 'StimDLC','epochinfo','yes');
    
    EEGstimURO = pop_epoch( EEGref, {'ActionBeg-palmUp-Right-Open'}, [-0.1 1],'newname', 'StimURO','epochinfo','yes');
    EEGstimURC = pop_epoch( EEGref, {'ActionBeg-palmUp-Right-Close'}, [-0.1 1],'newname', 'StimURC','epochinfo','yes');
    EEGstimULO = pop_epoch( EEGref, {'ActionBeg-palmUp-Left-Open'}, [-0.1 1],'newname', 'StimULO','epochinfo','yes');
    EEGstimULC = pop_epoch( EEGref, {'ActionBeg-palmUp-Left-Close'}, [-0.1 1],'newname', 'StimULC','epochinfo','yes');
    
    EEGstimIRO = pop_epoch( EEGref, {'ActionBeg-palmIn-Right-Open'}, [-0.1 1],'newname', 'StimIRO','epochinfo','yes');
    EEGstimIRC = pop_epoch( EEGref, {'ActionBeg-palmIn-Right-Close'}, [-0.1 1],'newname', 'StimIRC','epochinfo','yes');
    EEGstimILO = pop_epoch( EEGref, {'ActionBeg-palmIn-Left-Open'}, [-0.1 1],'newname', 'StimILO','epochinfo','yes');
    EEGstimILC = pop_epoch( EEGref, {'ActionBeg-palmIn-Left-Close'}, [-0.1 1],'newname', 'StimILC','epochinfo','yes');

    
    EEGstimWW = pop_epoch( EEGref, {'StCF_____EVNT_1'}, [-0.1 2],'newname', 'StimWW','epochinfo','yes');
    EEGstimWL = pop_epoch( EEGref, {'StCF_____EVNT_2'}, [-0.1 2],'newname', 'StimWL','epochinfo','yes');
    EEGstimLL = pop_epoch( EEGref, {'StCF_____EVNT_3'}, [-0.1 2],'newname', 'StimLL','epochinfo','yes');
    EEGstimLW = pop_epoch( EEGref, {'StCF_____EVNT_4'}, [-0.1 2],'newname', 'StimLW','epochinfo','yes');

    EEGfeedWW = pop_epoch( EEGref, {'FBCF_____EVNT_1'}, [-0.1 0.7],'newname', 'FeedWW','epochinfo','yes');
    EEGfeedWL = pop_epoch( EEGref, {'FBCF_____EVNT_2'}, [-0.1 0.7],'newname', 'FeedWL','epochinfo','yes');
    EEGfeedLL = pop_epoch( EEGref, {'FBCF_____EVNT_3'}, [-0.1 0.7],'newname', 'FeedLL','epochinfo','yes');
    EEGfeedLW = pop_epoch( EEGref, {'FBCF_____EVNT_4'}, [-0.1 0.7],'newname', 'FeedLW','epochinfo','yes');
    
    
    event0=find(strcmp('0',{EEGstimDRO.event.mffkey_eval}));
    event1=find(strcmp('1',{EEGstimWW.event.mffkey_eval}));
    EEGstimWW0=pop_selectevent(EEGstimWW,'event',event0);
    EEGstimWW1=pop_selectevent(EEGstimWW,'event',event1);

    event0=find(strcmp('0',{EEGstimWL.event.mffkey_eval}));
    event1=find(strcmp('1',{EEGstimWL.event.mffkey_eval}));
    EEGstimWL0=pop_selectevent(EEGstimWL,'event',event0);
    EEGstimWL1=pop_selectevent(EEGstimWL,'event',event1);

    event0=find(strcmp('0',{EEGstimLL.event.mffkey_eval}));
    event1=find(strcmp('1',{EEGstimLL.event.mffkey_eval}));
    EEGstimLL0=pop_selectevent(EEGstimLL,'event',event0);
    EEGstimLL1=pop_selectevent(EEGstimLL,'event',event1);

    event0=find(strcmp('0',{EEGstimLW.event.mffkey_eval}));
    event1=find(strcmp('1',{EEGstimLW.event.mffkey_eval}));
    EEGstimLW0=pop_selectevent(EEGstimLW,'event',event0);
    EEGstimLW1=pop_selectevent(EEGstimLW,'event',event1);

    event0=find(strcmp('0',{EEGfeedWW.event.mffkey_eval}));
    event1=find(strcmp('1',{EEGfeedWW.event.mffkey_eval}));
    EEGfeedWW0=pop_selectevent(EEGfeedWW,'event',event0);
    EEGfeedWW1=pop_selectevent(EEGfeedWW,'event',event1);

    event0=find(strcmp('0',{EEGfeedWL.event.mffkey_eval}));
    event1=find(strcmp('1',{EEGfeedWL.event.mffkey_eval}));
    EEGfeedWL0=pop_selectevent(EEGfeedWL,'event',event0);
    EEGfeedWL1=pop_selectevent(EEGfeedWL,'event',event1);

    event0=find(strcmp('0',{EEGfeedLL.event.mffkey_eval}));
    event1=find(strcmp('1',{EEGfeedLL.event.mffkey_eval}));
    EEGfeedLL0=pop_selectevent(EEGfeedLL,'event',event0);
    EEGfeedLL1=pop_selectevent(EEGfeedLL,'event',event1);

    event0=find(strcmp('0',{EEGfeedLW.event.mffkey_eval}));
    event1=find(strcmp('1',{EEGfeedLW.event.mffkey_eval}));
    EEGfeedLW0=pop_selectevent(EEGfeedLW,'event',event0);
    EEGfeedLW1=pop_selectevent(EEGfeedLW,'event',event1);

    EEGstimWW0ref = pop_reref( EEGstimWW0,'E129');
    EEGstimWW1ref = pop_reref( EEGstimWW1,'E129');
    EEGstimWL0ref = pop_reref( EEGstimWL0,'E129');
    EEGstimWL1ref = pop_reref( EEGstimWL1,'E129');
    EEGstimLW0ref = pop_reref( EEGstimLW0,'E129');
    EEGstimLW1ref = pop_reref( EEGstimLW1,'E129');
    EEGstimLL0ref = pop_reref( EEGstimLL0,'E129');
    EEGstimLL1ref = pop_reref( EEGstimLL1,'E129');

    EEGfeedWW0ref = pop_reref( EEGfeedWW0,'E129');
    EEGfeedWW1ref = pop_reref( EEGfeedWW1,'E129');
    EEGfeedWL0ref = pop_reref( EEGfeedWL0,'E129');
    EEGfeedWL1ref = pop_reref( EEGfeedWL1,'E129');
    EEGfeedLW0ref = pop_reref( EEGfeedLW0,'E129');
    EEGfeedLW1ref = pop_reref( EEGfeedLW1,'E129');
    EEGfeedLL0ref = pop_reref( EEGfeedLL0,'E129');
    EEGfeedLL1ref = pop_reref( EEGfeedLL1,'E129');

    [EEGstimWW0ar, rmepochs] = pop_autorej ( EEGstimWW0ref, 'threshold', 75, 'electrodes', [1:64], 'startprob', 5, 'maxrej', 20, 'nogui',['on'])
    [EEGstimWW1ar, rmepochs] = pop_autorej ( EEGstimWW1ref, 'threshold', 75, 'electrodes', [1:128], 'startprob', 5, 'maxrej', 20, 'nogui',['on'])
    [EEGstimWL0ar, rmepochs] = pop_autorej ( EEGstimWL0ref, 'threshold', 75, 'electrodes', [1:128], 'startprob', 5, 'maxrej', 20, 'nogui',['on'])
    [EEGstimWL1ar, rmepochs] = pop_autorej ( EEGstimWL1ref, 'threshold', 75, 'electrodes', [1:128], 'startprob', 5, 'maxrej', 20, 'nogui',['on'])
    [EEGstimLW0ar, rmepochs] = pop_autorej ( EEGstimLW0ref, 'threshold', 75, 'electrodes', [1:128], 'startprob', 5, 'maxrej', 20, 'nogui',['on'])
    [EEGstimLW1ar, rmepochs] = pop_autorej ( EEGstimLW1ref, 'threshold', 75, 'electrodes', [1:128], 'startprob', 5, 'maxrej', 20, 'nogui',['on'])
    [EEGstimLL0ar, rmepochs] = pop_autorej ( EEGstimLL0ref, 'threshold', 75, 'electrodes', [1:128], 'startprob', 5, 'maxrej', 20, 'nogui',['on'])
    [EEGstimLL1ar, rmepochs] = pop_autorej ( EEGstimLL1ref, 'threshold', 75, 'electrodes', [1:128], 'startprob', 5, 'maxrej', 20, 'nogui',['on'])

    [EEGfeedWW0ar, rmepochs] = pop_autorej ( EEGfeedWW0ref, 'threshold', 75, 'electrodes', [1:128], 'startprob', 5, 'maxrej', 20, 'nogui',['on'])
    [EEGfeedWW1ar, rmepochs] = pop_autorej ( EEGfeedWW1ref, 'threshold', 75, 'electrodes', [1:128], 'startprob', 5, 'maxrej', 20, 'nogui',['on'])
    [EEGfeedWL0ar, rmepochs] = pop_autorej ( EEGfeedWL0ref, 'threshold', 75, 'electrodes', [1:128], 'startprob', 5, 'maxrej', 20, 'nogui',['on'])
    [EEGfeedWL1ar, rmepochs] = pop_autorej ( EEGfeedWL1ref, 'threshold', 75, 'electrodes', [1:128], 'startprob', 5, 'maxrej', 20, 'nogui',['on'])
    [EEGfeedLW0ar, rmepochs] = pop_autorej ( EEGfeedLW0ref, 'threshold', 75, 'electrodes', [1:128], 'startprob', 5, 'maxrej', 20, 'nogui',['on'])
    [EEGfeedLW1ar, rmepochs] = pop_autorej ( EEGfeedLW1ref, 'threshold', 75, 'electrodes', [1:128], 'startprob', 5, 'maxrej', 20, 'nogui',['on'])
    [EEGfeedLL0ar, rmepochs] = pop_autorej ( EEGfeedLL0ref, 'threshold', 75, 'electrodes', [1:128], 'startprob', 5, 'maxrej', 20, 'nogui',['on'])
    [EEGfeedLL1ar, rmepochs] = pop_autorej ( EEGfeedLL1ref, 'threshold', 75, 'electrodes', [1:128], 'startprob', 5, 'maxrej', 20, 'nogui',['on'])

    % Drift/baseline correction
    EEGstimWW0bc = pop_rmbase (EEGstimWW0ar, [-100 0]);
    EEGstimWW1bc = pop_rmbase (EEGstimWW1ar, [-100 0]);
    EEGstimWL0bc = pop_rmbase (EEGstimWL0ar, [-100 0]);
    EEGstimWL1bc = pop_rmbase (EEGstimWL1ar, [-100 0]);
    EEGstimLW0bc = pop_rmbase (EEGstimLW0ar, [-100 0]);
    EEGstimLW1bc = pop_rmbase (EEGstimLW1ar, [-100 0]);
    EEGstimLL0bc = pop_rmbase (EEGstimLL0ar, [-100 0]);
    EEGstimLL1bc = pop_rmbase (EEGstimLL1ar, [-100 0]);

    EEGfeedWW0bc = pop_rmbase (EEGfeedWW0ar, [-100 0]);
    EEGfeedWW1bc = pop_rmbase (EEGfeedWW1ar, [-100 0]);
    EEGfeedWL0bc = pop_rmbase (EEGfeedWL0ar, [-100 0]);
    EEGfeedWL1bc = pop_rmbase (EEGfeedWL1ar, [-100 0]);
    EEGfeedLW0bc = pop_rmbase (EEGfeedLW0ar, [-100 0]);
    EEGfeedLW1bc = pop_rmbase (EEGfeedLW1ar, [-100 0]);
    EEGfeedLL0bc = pop_rmbase (EEGfeedLL0ar, [-100 0]);
    EEGfeedLL1bc = pop_rmbase (EEGfeedLL1ar, [-100 0]);
    %}
    %save(['Preprocessed/cf_',fileName(1:end-3),'mat'],'EEG*');
    %}
end