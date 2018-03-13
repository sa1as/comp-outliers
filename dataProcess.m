testfiledir1 = '/home/saias/Documents/composition/acoustic data/acoustic 1';
testfiledir2 = '/home/doltsinis/Documents/Composition/acoustic data/acoustic 2';
testfiledir4 = '/home/doltsinis/Documents/Composition/acoustic data/acoustic 4';

wavfiles = dir(fullfile(testfiledir1, '*.wav'));
nfiles = length(wavfiles);
%data  = cell(nfiles);
for i = 1 : floor(nfiles/40)
   %fid = fopen( fullfile(testfiledir, matfiles(i).name) );
   %data{i} = fscanf(fid,'%c');
   i
   data(:,i) = audioread(wavfiles(i).name); % import data fiels(.wav)
   %fclose(fid);
end

data1 = data;
data2 = data;
data4 = data;

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
sampleNum = 5;
singalSize = length(data(:,1));
dataSetSize = length(data(1,:));

for i = 1:5 %dataSetSize % run through the data set
    counter = 1;
    
    for j = 1:singalSize %run through every signal (20 sec)
        windowsMedian(counter) = median(data(j, i:i+sampleNum)); % median of the n sample numbers
        
        windowCounter = 1;
        newWindow = zeros(1,k);
        
        for k = sampleNum:-1:1
            newWindow(windowCounter) = abs(data(j,k) - windowsMedian(counter));
            windowCounter = windowCounter + 1;
        end
        
        MAD(i,counter) = median(newWindow); % MAD[r,c] -> c are the data points within a 20 sec signal
        counter = counter + 1;
    end
        
end

% calculate LOF (Local Outlier Factor)


