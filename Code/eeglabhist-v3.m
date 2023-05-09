% EEGLAB history file generated on the 17-Mar-2023
% ------------------------------------------------

EEG.etc.eeglabvers = '2022.0'; % this tracks which version of EEGLAB is being used, you may ignore it
EEG = pop_loadxdf('/mnt/sda1/shivam/Thesis/Grasp Experiment/Data/Raw/FP02.xdf' , 'streamtype', 'EEG', 'exclude_markerstreams', {});
EEG = eeg_checkset( EEG );
EEG=pop_chanedit(EEG, 'load',{'/mnt/sda1/shivam/Thesis/Grasp Experiment/Data/ChannelLocations/AdultAverageNet64_v1.sfp','filetype','autodetect'},'changefield',{68,'datachan',0});
EEG = eeg_checkset( EEG );
figure; topoplot([],EEG.chanlocs, 'style', 'blank',  'electrodes', 'numpoint', 'chaninfo', EEG.chaninfo);
EEG = pop_eegfiltnew(EEG, 'locutoff',1,'hicutoff',40,'plotfreqz',1);
EEG = eeg_checkset( EEG );
EEG = pop_clean_rawdata(EEG, 'FlatlineCriterion',10,'ChannelCriterion',0.8,'LineNoiseCriterion',4,'Highpass','off','BurstCriterion',20,'WindowCriterion','off','BurstRejection','off','Distance','Euclidian');
EEG = eeg_checkset( EEG );
EEG = eeg_checkset( EEG );
EEG = eeg_checkset( EEG );
EEG = pop_reref( EEG, []);
EEG = eeg_checkset( EEG );
EEG = pop_rmbase( EEG, [],[]);
EEG = eeg_checkset( EEG );
pop_eegplot( EEG, 1, 1, 1);
