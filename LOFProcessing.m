for i=1:length(data(1,:))
    energy(i)= sumabs(data(:,i).^2)/(length(data(:,i)));
    skew(i) = skewness( data(:,i) );%/length(Signal);
end


%dataset.trainx = randi(100, 100,1);
%dataset.testx = randi(200,10,1);


for j=5:20
    params.minptslb = j;
    params.minptsub = j;
    params.theta = 2;

    for i = 1:length(energy)-j-1

        dataset.trainx = [energy(1, (i:i+j) )' skew(1, (i:i+j) )'];
    
        dataset.testx = [energy(1, (i+j+1) )' skew(1, (i+j+1) )'];
        %dataset.testx = energy(i+11)';
    

     results{j}(i) = LocalOutlierFactor(dataset, params);
    end
    outNum(j-4) = sum([results{1, j}.y]) - length([results{1, j}.y]);
end
bar(outNum)



