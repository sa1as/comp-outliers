testfiledir1 = '/home/doltsinis/Documents/Composition/acoustic data/acoustic 1';
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

% calculate Median Absolut Deviation (MAD)

for i = 1:length(data)
    dataMedian = median(data(:,i));
    for j=1:length(data(:,1))
        pointMedian = ( data(j,i) - dataMedian);
        pointMedianAbs = abs(( data(j,i) - dataMedian));
    end
    MADAbs(i) = median(pointMedianAbs);
    MAD(i) = median(pointMedian);

end

% calculate LOF (Local Outlier Factor)


