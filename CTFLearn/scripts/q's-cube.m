%this a qubigami decoding
% input:
%       text file contain a square hex cipher   
%       sguare dimesion should be (2*2 4*4 8*8 16*16 ...) 
% output:
%       message text file 
clc;
clear;
Dim=16;
%------------------read file and convert to matrix----------------
tic
ID=fopen('cipher.txt');
cell=textscan(ID,'%s','Delimiter','\n');
p=cell{1,1};
str_hex = string(cell2mat(p));
sqr=split(str_hex,'');
msg=hex2dec(sqr(:,2:end-1));
%--------------------------

plc_fold_horz=Dim/2;
plc_fold_ver=Dim/2;
final_hight=Dim^2;
%-------------------------first up2down fold-------------------------------
rev_half1=flip(flipud(msg(1:plc_fold_horz,:)),3);
fix_half2=msg(plc_fold_horz+1:end,:,:);
u2d_open=cat(3,fix_half2,rev_half1);
%---------------------------first left2right fold--------------------------
rev_half1=flip(fliplr(u2d_open(:,1:plc_fold_ver,:)),3);
fix_half2=u2d_open(:,plc_fold_ver+1:end,:); 
l2r_open=cat(3,fix_half2,rev_half1);

while plc_fold_horz~=1 && plc_fold_ver~=1 
plc_fold_horz=plc_fold_horz/2;
rev_half1=flip(flipud(l2r_open(1:plc_fold_horz,:,:)),3);
fix_half2=l2r_open(plc_fold_horz+1:end,:,:);
u2d_open=cat(3,fix_half2,rev_half1);

plc_fold_ver=plc_fold_ver/2;
rev_half1=flip(fliplr(u2d_open(:,1:plc_fold_ver,:)),3);
fix_half2=u2d_open(:,plc_fold_ver+1:end,:); 
l2r_open=cat(3,fix_half2,rev_half1);
end
c=zeros(1,final_hight);
k=final_hight;
for i=1:final_hight
    c(1,i)=l2r_open(1,1,k);    %reading letters from  up to down(end to begin)
    k=k-1;
end
cipher_hex=join(dec2hex(c)');
half1=cipher_hex(1:2:end);
half2=cipher_hex(2:2:end);
cipher=char(hex2dec(([half1;half2])'))';
fprintf(cipher)
toc

