% EEGLAB history file generated on the 16-Mar-2023
% ------------------------------------------------

EEG.etc.eeglabvers = '2022.0'; % this tracks which version of EEGLAB is being used, you may ignore it
EEG = pop_loadxdf('/mnt/sda1/shivam/Thesis/Grasp Experiment/Data/Raw/FP02.xdf' , 'streamtype', 'EEG', 'exclude_markerstreams', {});
EEG = eeg_checkset( EEG );
EEG=pop_chanedit(EEG, 'lookup','/mnt/sda1/shivam/softwares/eeglab2022.0/plugins/dipfit/standard_BEM/elec/standard_1005.elc','load',{'/mnt/sda1/shivam/Thesis/Grasp Experiment/Data/ChannelLocations/AdultAverageNet64_v1.sfp','filetype','autodetect'},'changefield',{68,'datachan',0});
EEG = eeg_checkset( EEG );
pop_eegplot( EEG, 1, 1, 1);
figure; pop_spectopo(EEG, 1, [0  1844831], 'EEG' , 'freq', [6 10 22], 'freqrange',[0.1 60],'electrodes','off');
EEG = pop_eegfiltnew(EEG, 'locutoff',1,'hicutoff',40,'plotfreqz',1);
EEG = eeg_checkset( EEG );
pop_eegplot( EEG, 1, 1, 1);
figure; pop_spectopo(EEG, 1, [0  1844831], 'EEG' , 'freq', [6 10 22], 'freqrange',[0.1 60],'electrodes','off');
EEG = pop_clean_rawdata(EEG, 'FlatlineCriterion',5,'ChannelCriterion',0.8,'LineNoiseCriterion',4,'Highpass','off','BurstCriterion',20,'WindowCriterion',0.25,'BurstRejection','on','Distance','Euclidian','WindowCriterionTolerances',[-Inf 7] );
EEG = eeg_checkset( EEG );
pop_eegplot( EEG, 1, 1, 1);
figure; pop_spectopo(EEG, 1, [0      1635376.1135], 'EEG' , 'freq', [6 10 22], 'freqrange',[0.1 60],'electrodes','off');
EEG = pop_epoch( EEG, {  'ActionBeg-palmDown-Left-Close'  'ActionBeg-palmDown-Left-Open'  'ActionBeg-palmDown-Right-Close'  'ActionBeg-palmDown-Right-Open'  'ActionBeg-palmIn-Left-Close'  'ActionBeg-palmIn-Left-Open'  'ActionBeg-palmIn-Right-Close'  'ActionBeg-palmIn-Right-Open'  'ActionBeg-palmUp-Left-Close'  'ActionBeg-palmUp-Left-Open'  'ActionBeg-palmUp-Right-Close'  'ActionBeg-palmUp-Right-Open'  'FixBeg-palmDown-Left-Close'  'FixBeg-palmDown-Left-Open'  'FixBeg-palmDown-Right-Close'  'FixBeg-palmDown-Right-Open'  'FixBeg-palmIn-Left-Close'  'FixBeg-palmIn-Left-Open'  'FixBeg-palmIn-Right-Close'  'FixBeg-palmIn-Right-Open'  'FixBeg-palmUp-Left-Close'  'FixBeg-palmUp-Left-Open'  'FixBeg-palmUp-Right-Close'  'FixBeg-palmUp-Right-Open'  'FreeFixBeg'  'FreeHandBeg'  }, [-0.1           1], 'epochinfo', 'yes');
EEG = eeg_checkset( EEG );
EEG = pop_rmbase( EEG, [-100 0] ,[]);
EEG = eeg_checkset( EEG );
figure; pop_spectopo(EEG, 1, [-100  999], 'EEG' , 'freq', [6 10 22], 'freqrange',[0.1 60],'electrodes','off');
