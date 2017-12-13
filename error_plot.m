function [] = error_plot(x,y,err,th, plot_title)
figure;
hold on;
e = errorbar(x,y,err);
plot(x,th*ones(size(x)),'LineWidth',2);
hold off;
title(plot_title);
box off;
xlim([0 x(end)]);
ylim([0 th+1]);
set(gca,'XTick',0:1:x(end));
xlabel('Hours of the day');
ylabel('Speed [Mb/s]');
e.Marker = '.';
e.MarkerSize = 30;
e.CapSize = 15;
end