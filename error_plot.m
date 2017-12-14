function [] = error_plot(x,y,err,th, plot_title)
figure;
hold on;
e = errorbar(x,y,err);
plot(x,th*ones(size(x)),'LineWidth',2);
hold off;
title(plot_title);
box off;
xlim([0 x(end)]);
ymax = max(th+1,th+0.2*th);
ylim([0 ymax]);
set(gca,'XTick',0:1:x(end));
xlabel('Hours of the day');
ylabel('Speed [Mb/s]');
legend('measures','theoretical');
e.Marker = '.';
e.MarkerSize = 30;
e.CapSize = 15;
end