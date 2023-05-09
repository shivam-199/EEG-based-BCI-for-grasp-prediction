fileList = dir('./Raw/*.xdf');

for i=1:size(fileList)
%% Reading files, adding channel location, filter, resampling, clean artifact, interpolation, rereferencing
    fileName=fileList(i).name;
    EEG = pop_loadxdf(strcat(fileList(i).folder, "/", fileName) , 'streamtype', 'EEG', 'exclude_markerstreams', {});
    EEG = eeg_checkset( EEG );
    
    EEG=pop_chanedit(EEG, 'load',{'/mnt/sda1/shivam/Thesis/Grasp Experiment/Data/ChannelLocations/AdultAverageNet64_v1.sfp','filetype','autodetect'},'changefield',{68,'datachan',0});
    EEG = eeg_checkset( EEG );
    
    EEG = pop_eegfiltnew(EEG, 'locutoff',1,'hicutoff',40,'plotfreqz',1);
    EEG = eeg_checkset( EEG );
    
    %EEG = pop_clean_rawdata(EEG, 'FlatlineCriterion',5,'ChannelCriterion',0.8,'LineNoiseCriterion',4,'Highpass','off','BurstCriterion',20,'WindowCriterion',0.25,'BurstRejection','on','Distance','Euclidian','WindowCriterionTolerances',[-Inf 7] );
    EEG = pop_clean_rawdata(EEG, 'FlatlineCriterion',10,'ChannelCriterion',0.8,'LineNoiseCriterion',4,'Highpass','off','BurstCriterion',20,'WindowCriterion','off','BurstRejection','off','Distance','Euclidian');
    EEG = eeg_checkset( EEG );
    
    
    EEG = pop_reref( EEG, []);
    EEG = eeg_checkset( EEG );
    %EEG = pop_epoch( EEG, {  'ActionBeg-palmDown-Left-Close'  'ActionBeg-palmDown-Left-Open'  'ActionBeg-palmDown-Right-Close'  'ActionBeg-palmDown-Right-Open'  'ActionBeg-palmIn-Left-Close'  'ActionBeg-palmIn-Left-Open'  'ActionBeg-palmIn-Right-Close'  'ActionBeg-palmIn-Right-Open'  'ActionBeg-palmUp-Left-Close'  'ActionBeg-palmUp-Left-Open'  'ActionBeg-palmUp-Right-Close'  'ActionBeg-palmUp-Right-Open'  'FixBeg-palmDown-Left-Close'  'FixBeg-palmDown-Left-Open'  'FixBeg-palmDown-Right-Close'  'FixBeg-palmDown-Right-Open'  'FixBeg-palmIn-Left-Close'  'FixBeg-palmIn-Left-Open'  'FixBeg-palmIn-Right-Close'  'FixBeg-palmIn-Right-Open'  'FixBeg-palmUp-Left-Close'  'FixBeg-palmUp-Left-Open'  'FixBeg-palmUp-Right-Close'  'FixBeg-palmUp-Right-Open'  'FreeFixBeg'  'FreeHandBeg'  }, [-0.1           1], 'epochinfo', 'yes');
    %EEG = eeg_checkset( EEG );
    
    EEG = pop_rmbase( EEG, []);
    EEG = eeg_checkset( EEG );
    
    %% Saving preprocessed data
    EEG = pop_saveset(EEG, 'filename', fileName(1:end-4), 'filepath', '/mnt/sda1/shivam/Thesis/Grasp Experiment/Data/PreprocessedData/Preprocess HAPPE');
    
end