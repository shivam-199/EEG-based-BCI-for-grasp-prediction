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
pop_eegplot( EEG, 1, 1, 1);
EEG = eeg_checkset( EEG );
EEG = pop_eegthresh(EEG,1,[1:64] ,-75,75,-0.1,0.999,0,0);
EEG = eeg_checkset( EEG );
EEG = pop_rejtrend(EEG,1,[1:64] ,1100,5,0.05,0,0);
EEG = pop_rejtrend(EEG,1,[1:64] ,1100,50,0.3,0,0);
EEG = eeg_checkset( EEG );
EEG = pop_jointprob(EEG,1,[1:64] ,5,5,0,0,0,[],0);
EEG = pop_jointprob(EEG,1,[1:64] ,5,5,0,0,'set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''mantrial''), ''string'', num2str(sum(EEG.reject.rejmanual)));set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''threshtrial''), ''string'', num2str(sum(EEG.reject.rejthresh)));set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''freqtrial''), ''string'', num2str(sum(EEG.reject.rejfreq)));set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''consttrial''), ''string'', num2str(sum(EEG.reject.rejconst)));set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''enttrial''), ''string'', num2str(sum(EEG.reject.rejjp)));set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''kurttrial''), ''string'', num2str(sum(EEG.reject.rejkurt)));',[],0);
EEG = pop_rejkurt(EEG,1,[1:64] ,5,5,0,0,0,[],0);
EEG = pop_rejkurt(EEG,1,[1:64] ,5,5,0,0,'set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''mantrial''), ''string'', num2str(sum(EEG.reject.rejmanual)));set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''threshtrial''), ''string'', num2str(sum(EEG.reject.rejthresh)));set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''freqtrial''), ''string'', num2str(sum(EEG.reject.rejfreq)));set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''consttrial''), ''string'', num2str(sum(EEG.reject.rejconst)));set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''enttrial''), ''string'', num2str(sum(EEG.reject.rejjp)));set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''kurttrial''), ''string'', num2str(sum(EEG.reject.rejkurt)));',[],0);
EEG = pop_rejspec( EEG, 1,'elecrange',[1:64] ,'method','multitaper','threshold',[-50 50] ,'freqlimits',[0 2] ,'eegplotcom','set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''mantrial''), ''string'', num2str(sum(EEG.reject.rejmanual)));set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''threshtrial''), ''string'', num2str(sum(EEG.reject.rejthresh)));set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''freqtrial''), ''string'', num2str(sum(EEG.reject.rejfreq)));set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''consttrial''), ''string'', num2str(sum(EEG.reject.rejconst)));set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''enttrial''), ''string'', num2str(sum(EEG.reject.rejjp)));set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''kurttrial''), ''string'', num2str(sum(EEG.reject.rejkurt)));','eegplotplotallrej',0,'eegplotreject',0);
EEG = pop_rejkurt(EEG,1,[1:64] ,5,5,0,0,'set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''mantrial''), ''string'', num2str(sum(EEG.reject.rejmanual)));set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''threshtrial''), ''string'', num2str(sum(EEG.reject.rejthresh)));set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''freqtrial''), ''string'', num2str(sum(EEG.reject.rejfreq)));set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''consttrial''), ''string'', num2str(sum(EEG.reject.rejconst)));set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''enttrial''), ''string'', num2str(sum(EEG.reject.rejjp)));set(findobj(''parent'', findobj(''tag'', ''rejtrialraw''), ''tag'', ''kurttrial''), ''string'', num2str(sum(EEG.reject.rejkurt)));',[],0);
EEG = eeg_rejsuperpose( EEG, 1, 1, 1, 1, 1, 1, 1, 1);
EEG = pop_rejepoch( EEG, [5 6 8 12 14 15 16 19 24 28 29 31 33 34 35 38 39 45 49 51 53 54 56 60 64 65 67 69 73 76 79 83 84 85 89 91 92 94 99 100 101 105 110 113 119 123 124 125 127 130 132 133 136 138 140 141 147 148 151 152 156 157:159 161 162 163 166 169 170 172 178 180 181 185 187 189 190 191 195 196 198:2:202 203 204 207 208 209 211 212:215 218 219:221 223 224 225 229 230:234 236 237:239 241 242 245 246 247 250 251 254 255:257 259 260 261 264 265 267 269 270 273 275 276:278 281 282 283 285 287 288:290 293 294:300 302 305 306 307 311 312 313 316 317:322 324 325:328 331 332 333 338 339 341 342 345 346 347 349 350:353 355:2:359 362 366 367 370 371 373 374 375 377 378 380 381 382 384 388 391 392:394 398 400 401 403 408 409 414 415 418 419:422 424 425 427 428:431 433 434:439 444 447 448:453 456 457 459 460:467 471 472 474 476 477 479 482 483 484 486 487 490 491:495 497 498 501 504 505 506 509 510 513 514 516 517:520 524 525 526 528 529:534 536 537:541 543 546 547 548 550 551 552 554 556 557:560 562 563 565 567 570 571 573 574:576 578 579 584 587 589 591 594 595 598 599 600 605 606:609 611 612:615 617 619 624 625 627 628 630 631:633 635 636:641 643 644:646 648 649:651 653 654:657 659 660:663 665 666 667 670 672 677 678:685 687 688:697 701 702:712 714 715:722 726 728 729 731 732 734 735 739 741 742 743 745 747 748:753 755 756:763 765 766 767 769 770 772 774 775 777 778 779 781 782 785 787 788:790 795 796 798:2:802 803:805 807 809 810:815 819 821 823 824:831 833 834:837 839 840 841 843 844 846 847 848 850 851 852 858 859:861] ,0);
EEG = eeg_checkset( EEG );
EEG = eeg_checkset( EEG );
pop_eegplot( EEG, 1, 1, 1);
figure; pop_spectopo(EEG, 1, [-100  999], 'EEG' , 'freq', [6 10 22], 'freqrange',[01 60],'electrodes','off');
