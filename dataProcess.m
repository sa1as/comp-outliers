testfiledir1 = '/home/saias/Documents/composition/acoustic data/acoustic 1';
testfiledir2 = '/home/saias/Documents/composition/acoustic data/acoustic 2';
testfiledir4 = '/home/saias/Documents/composition/acoustic data/acoustic 4';

wavfiles = dir(fullfile(testfiledir1, '*.wav'));
nfiles = length(wavfiles);
%data  = cell(nfiles);
for i = 1 : floor(nfiles/10)
   %fid = fopen( fullfile(testfiledir, matfiles(i).name) );
   %data{i} = fscanf(fid,'%c');
   i
   data(:,i) = audioread(wavfiles(i).name); % import data fiels(.wav)
   %fclose(fid);
end

data1 = data(40000:end,:);
data2 = data(40000:end,:);
data4 = data(40000:end,:);

% visualization 
plotData1 = [data1(:,15); data1(end,15)*ones(1000000,1); data1(:,16); data1(end,16)*ones(1000000,1); data1(:,17)];
subplot(3,1,1)
plot(plotData1)

plotData2 = [data2(:,15); data2(end,15)*ones(1000000,1); data2(:,16); data1(end,16)*ones(1000000,1); data2(:,17)];
subplot(3,1,2)
plot(plotData2)

plotData4 = [data4(:,15); data2(end,15)*ones(1000000,1); data4(:,16); data1(end,16)*ones(1000000,1); data4(:,17)];
subplot(3,1,3)
plot(plotData4)

%% outlier algorithms

% calculate Median Absolut Deviation (MAD) based on time poins, for K
% signals
data = data1;
sampleNum = 5;
singalSize = length(data(:,1));
dataSetSize = length(data(1,:));
%dataSetSize = 10;
num = 1;
numAlt = 1;


for i = 1:dataSetSize % run through the data set
    counter = 1;
    
    for j = 1:singalSize %run through every signal (20 sec)
        windowsMedian = median(data(j, i:i+sampleNum)); % median of the n sample numbers
        MAD(i,counter) = median(abs(data(j, i:i+sampleNum) - windowsMedian ));
        

        %modZ(i,counter) = (data(j, i:i+sampleNum) - windowsMedian)/1.4826*MAD(i,counter);

     
        AltwindowsMedian = median(data(j, i:i+sampleNum)); % median of the n sample numbers
        AltMAD(i,counter) = median(abs(data(j, 1:i+sampleNum) - AltwindowsMedian ));
        %modZAlt(i,counter) = (data(j, 1:i+sampleNum) - median(data(j, 1:i+sampleNum)) )/1.4826*AltMAD(i,counter);
   


        
 % MAD[r,c] -> c are the data points within a 20 sec signal
 
        %if abs(modZ(i,counter)) > 3  
         %   SampleAbnormalities(num) = i;
          %  Abnormalities(num) = j;
          %  num = num +1
        %end
        
       % if abs(modZAlt(i,counter)) > 3
         %   SampleAbnormalitiesAlt(num) = i;
         %   AbnormalitiesAlt(num) = j;
        %    numAlt = numAlt +1
       % end
        
        
        counter = counter + 1;
    end
        i
        
end



% calculate LOF (Local Outlier Factor)

boxplot(AltMAD(:,randi(160,10,1)))
