fileList = dir('./Raw/*.xdf');

for i=1:size(fileList)
    %% Reading files, adding channel location, filter, resampling, clean artifact, interpolation, rereferencing
    fileName=fileList(i).name;
    EEG = pop_loadxdf(strcat(fileList(i).folder, "/", fileName));
    chanLoc = readlocs('/mnt/sda1/shivam/Thesis/Grasp Experiment/Data/ChannelLocations/EGIAmpServer64Chan.loc');
    EEG.chanlocs = chanLoc;
    
    %% Filtering data
    EEG = pop_eegfiltnew(EEG, 1, [], [], false, [], 0);
    EEG = pop_eegfiltnew(EEG, [], 45, [], false, [], 0);
    
    %% ICA decomposition, artifact removal (ICLabel), and recontruction
    EEG = pop_runica(EEG, 'icatype', 'runica');
    
    % Run ICLabel
    EEG = pop_iclabel(EEG, 'Default');
    
    % Flag components as Artifact after ICLabel
    EEG = pop_icflag(EEG, [0 0; 0.9 1; 0.9 1; 0 0; 0 0; 0 0; 0 0]);
    
    % Flag artifacts for rejection and remove them from EEG data.
    rejected_comps = find(EEG.reject.gcompreject > 0);
    EEG = pop_subcomp(EEG, rejected_comps);
    
    %% Saving preprocessed data
    EEG = pop_saveset(EEG, 'filename', fileName(1:end-4), 'filepath', '/mnt/sda1/shivam/Thesis/Grasp Experiment/Data/PreprocessedData/Preprocessed v3');

end