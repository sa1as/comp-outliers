for i=1:length(data(1,:))
   energy(i) = sum(abs(data(:,i)));    
end


%dataset.trainx = randi(100, 100,1);
%dataset.testx = randi(200,10,1);


for i = 1:length(energy)

    dataset.trainx = energy(i:i+10)';
    dataset.testx = energy(i+11)';
    
    params.minptslb = 10;
    params.minptsub = 10;
    params.theta = 2;
    
    results(i) = LocalOutlierFactor(dataset, params);
end