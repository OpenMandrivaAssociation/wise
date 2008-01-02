%define name	wise
%define version	2.2.0
%define rel	5
%define release	%mkrel %{rel}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Comparisons of DNA and protein sequences
Group:		Sciences/Biology
License:	GPL
URL:		http://www.ebi.ac.uk/Wise2/doc_wise2.html
Source:		ftp://ftp.ebi.ac.uk/pub/software/wise2/%{name}%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Wise2 is a package focused on comparisons of biopolymers, commonly DNA and 
protein sequence. Wise2's particular forte is the comparison of DNA sequence 
at the level of its protein translation. This comparison allows the simulta-
neous prediction of say gene structure with homology based alignment.

The Wise2 package was principally written by Ewan Birney, who wrote the main
genewise and estwise programs. The protein comparison database search program
was written by Richard Copley using the underlying Wise2 libraries.
Wise2 also uses code from Sean Eddy for reading HMMs and
for Extreme value distribution fitting.

%prep
%setup -q -n %{name}%{version}

%build
cd src && %make CFLAGS="-c $RPM_OPT_FLAGS" realall

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_bindir}
install -m 755 src/models/{pswdb,psw,genewisedb,estwisedb,estwise,genewise,dba,dnal,genomewise} %{buildroot}%{_bindir}

install -d -m 755 %{buildroot}%{_datadir}/%{name}
install -m 644 wisecfg/* %{buildroot}%{_datadir}/%{name}

# configuration
install -d -m 755 %{buildroot}%{_sysconfdir}/profile.d
echo "export WISECONFIGDIR=%{_datadir}/%{name}" > %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh
echo "setenv WISECONFIGDIR %{_datadir}/%{name}" > %{buildroot}%{_sysconfdir}/profile.d/%{name}.csh

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README LICENSE docs
%{_bindir}/*
%{_datadir}/%{name}
%config(noreplace) %{_sysconfdir}/profile.d/*


