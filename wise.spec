%define name	wise
%define version	2.2.0
%define rel	9
%define release	%mkrel %{rel}

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Comparisons of DNA and protein sequences
Group:		Sciences/Biology
License:	GPL
URL:		http://www.ebi.ac.uk/Wise2/doc_wise2.html
Source0:	ftp://ftp.ebi.ac.uk/pub/software/wise2/%{name}%{version}.tar.bz2
Patch0:		fix_getline.patch

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
%patch0 -p0

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

%files
%doc README LICENSE docs
%{_bindir}/*
%{_datadir}/%{name}
%config(noreplace) %{_sysconfdir}/profile.d/*




%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 2.2.0-9mdv2011.0
+ Revision: 615450
- the mass rebuild of 2010.1 packages

* Mon Mar 15 2010 Eric Fernandez <zeb@mandriva.org> 2.2.0-8mdv2010.1
+ Revision: 519888
- rebuild

* Wed Aug 19 2009 Eric Fernandez <zeb@mandriva.org> 2.2.0-7mdv2010.0
+ Revision: 417945
- compilation fix

* Wed May 06 2009 Eric Fernandez <zeb@mandriva.org> 2.2.0-6mdv2010.0
+ Revision: 372448
- rebuild

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 2.2.0-5mdv2008.1
+ Revision: 140932
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Aug 08 2007 Eric Fernandez <zeb@mandriva.org> 2.2.0-5mdv2008.0
+ Revision: 60257
- version number fix


* Tue Dec 19 2006 Eric Fernandez <zeb@mandriva.org> 2.2.0-4mdv2007.0
+ Revision: 100256
- Import wise

* Mon Jun 26 2006 Eric Fernandez <zeb@zebulon.org.uk> 2.2.0-4mdv2007.0
- rebuild
- use mkrel

* Fri Jul 29 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.2.0-3mdk
- spec cleanup

* Fri Jul 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 2.2.0-2mdk 
- rpmbuildupdate aware

* Sat Jan 24 2004 Guillaume Rousse <guillomovitch@mandrake.org> 2.2.0-1mdk
- first mdk release, after a spec file stolen from Luc Ducazu <luc@biolinux.org>

