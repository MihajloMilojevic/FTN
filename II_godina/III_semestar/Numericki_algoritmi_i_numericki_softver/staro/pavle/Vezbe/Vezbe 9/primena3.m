clc
clear all

worldSize = [10.0 10.0]; % [m]; dimenzije prostora

g = 9.81; % [m/s^2]; gravitaciono ubrzanje
airDensity = 1.225; % [kg/m^3]; gustina vazduha
rubberDensity = 1522; % [kg/m^3]; gustina gume
dragCoefficient = 0.47; % koeficijent aerodinami?nosti sfera

% sfere
sphereCount = 25;
r = (0.5 + rand(sphereCount, 1)*0.5)*0.5; % [m]; dimenzije sfera
A = r.^2*pi; % [m^2]; popre?ni preseci sfera
m = rubberDensity*4/3*r.^3*pi; % [kg]; mase (gumenih) sfera
v = zeros(sphereCount, 2); % [m/s]; trenutne brzine sfera
p = [(0.25 + rand(sphereCount, 1)*0.5)*worldSize(1) (0.75 + rand(sphereCount, 1)*0.5)*worldSize(2)]; % [m/s]; trenutni položaji sfera
colors = rand(sphereCount, 3); % (R,G,B); boje sfera

% GUI
fig = figure('Name', 'Collision', 'Units', 'normalized', 'Position', [0.2 0.2 0.6 0.6]); % prozor
axis([0 worldSize(1) 0 worldSize(2)]) % ograni?avanje prikaza u okviru dimenzija prostora
axis square % spre?avanje reskaliranja prikaza
axis off % sakrivanje osa

% inicijalizacija grafi?kih objekata
graphics = gobjects(4 + sphereCount);
% ivice
graphics(1) = line([0 worldSize(1)], [0 0], 'color', 'black');
graphics(2) = line([0 worldSize(1)], [worldSize(2) worldSize(2)], 'color', 'black');
graphics(3) = line([0 0], [0 worldSize(2)], 'color', 'black');
graphics(4) = line([worldSize(1) worldSize(1)], [0 worldSize(2)], 'color', 'black');
% sfere
for sphere = 1:sphereCount % za svaku sferu(sphere)
    location = p(sphere, :);
	radius = r(sphere);
	diameter = 2*radius;
	x = location(1) - radius;
	y = location(2) - radius;

	position = [x y diameter diameter];
    color = colors(sphere, :);
    % grafi?ki objekti od 1 do 4 su ivice
    graphics(4 + sphere) = rectangle('Position', position, 'Curvature', [1 1], 'EdgeColor', 'black', 'FaceColor', color);
end

% user force
rUser = min(worldSize)*0.2; % [m]
fUser = 15000; % [N = kg*m/s^2]
pUser = [-Inf -Inf]; % [m]
setappdata(gcf, 'mouseLocation', pUser) % inicijalizacija globalne promenljive

set(gcf, 'WindowButtonMotionFcn', @guiMouseMove); % registrovanje funkcije 

fps = 60; % broj osvežavanja prikaza u sekundi
timeScale = 1.0; % brzina simulacije

t1 = 0; % [s]; po?etni vremenski trenutak
dt = 1/fps; % [s]; vremenska razlika izme?u koraka
while ishandle(fig) % dokle god je prozor otvorent
    t2 = t1 + dt*timeScale; % naredni vremenski trenutak

    pUser = getappdata(gcf, 'mouseLocation'); % ?itanje vrednosti globalne promenljive

    % ažuriranje položaja i iscrtavanje
	for sphere = 1:sphereCount
        % sile
        % ----------------------------------------------------------------------
        FWeight = [0 -m(sphere)*g]; % težina tela (x, y)
 
        velocity = v(sphere, :);
        referenceArea = r(sphere)^2*pi;
        FDrag = -velocity*norm(velocity)*0.5*airDensity*dragCoefficient*A(sphere); % otpor vazduha (x, y)

        FUser = [0 0];
        direction = p(sphere, :) - pUser(1, 1:2);
        if norm(direction) <= rUser
            FUser = normalize(direction)*fUser; % korisni?ka sila (x, y)
        end

        F = FWeight + FDrag + FUser;

        % integracija
        % ----------------------------------------------------------------------
        ddpX = @(t, p, v) F(1)/m(sphere); % (p"(t) = F(t)/m) funkcija kretanja (x)
        ddpY = @(t, p, v) F(2)/m(sphere); % (p"(t) = F(t)/m) funkcija kretanja (y)
        [~, pnX] = eulerN(t1, t2, t2 - t1, [p(sphere, 1) v(sphere, 1)], ddpX, 0.0); % integracija (x)
        [~, pnY] = eulerN(t1, t2, t2 - t1, [p(sphere, 2) v(sphere, 2)], ddpY, 0.0); % integracija (y)
        p(sphere, :) = [pnX(1, end) pnY(1, end)]; % trenutni položaj
        v(sphere, :) = [pnX(2, end) pnY(2, end)]; % trenutna brzina

        % prikaz
        % ----------------------------------------------------------------------
        location = p(sphere, :);
        radius = r(sphere);
        diameter = 2*radius;
        x = location(1) - radius;
        y = location(2) - radius;

        position = [x y diameter diameter];
        set(graphics(4 + sphere), 'Position', position); % ažuriranje položaja grafi?kih objekata
	end

    t1 = t2; % prošli vremenski trenutak
    pause(dt);
end