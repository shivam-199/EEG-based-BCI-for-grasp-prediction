clear all; clc;
list_prt = dir('/DATAHDD/shivam/Thesis/Data/Preprocessed/ASR/matv1/*.mat');
root_path = '/DATAHDD/shivam/Thesis/Data/Preprocessed/ASR/matv1/';
tot_files = length(list_prt);
saveDir = '/DATAHDD/shivam/Thesis/Data/Preprocessed/ASR/Spectopo ASR/';

for participant = 1 : tot_files
    mat_file = list_prt(participant);
    mat_file_name = mat_file.name;
    parti = load([root_path, mat_file_name]);
    
    parti_name_split = split(mat_file_name, '.');
    parti_name = parti_name_split{1,1};
    
    data = parti.EEG;
    %data = resample(data, 125, 1000);
    %data = data.';
    srate = 1000;
    %channels = 64;

    spectra=[];
    shape = size(data);
    slice = data(:,1:srate);
    k = 1;
    for i = (srate+1) : srate : (shape(2)- srate)
        [spect, freqs] = spectopo(data(:,(i-srate):i), 0, srate, 'plot', 'off');
        spectra(k,:,:) = spect; % actual song order number wise
        k=k+1;
    end

    %spectra_shape = size(spectra)
    save([saveDir, parti_name,'_spec.mat'],'spectra');
end

% If getting error as - "UNDEFINED FUNCTION OR VARIABLE SPECTOPO", then run
% following command
% addpath('/home/brainlab/eeglab2019_1')
% eeglab