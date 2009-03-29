Summary: A portable NES/Famicom emulator
Name: fceultra
Version: 0.98.13
Release: 0.7.pre%{?dist}
License: GPLv2+
Group: Applications/Emulators
URL: http://fceultra.sourceforge.net/
Source: http://dl.sf.net/sourceforge/%{name}/fceu-%{version}-pre.src.tar.bz2
Patch0: fceultra-0.98.13-man.patch
Patch1: fceultra-0.98.13-cheatdir.patch
Patch2: fceultra-0.98.13-configure_fix_non_x86.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: SDL-devel >= 1.2.0
BuildRequires: libGLU-devel
BuildRequires: zlib-devel
BuildRequires: automake16

%description
FCE Ultra is a portable NES/Famicom emulator based on Bero's original
FCE source code. Large portions of it have been rewritten, resulting
in a much stabler and very compatible emulator.

%prep
%setup -q -n fceu
%patch0 -p1
%patch1 -p0
%patch2 -p1

perl -pi -e's/-mcpu=i686/\$(RPM_OPT_FLAGS)/' Makefile*
chmod 644 src/drivers/sexyal/convert.inc
mv Documentation/fceu-sdl.6 Documentation/fceultra.6

%build
%configure --with-opengl
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
install -m 755 src/fceu %{buildroot}%{_bindir}/fceultra
install -d %{buildroot}%_mandir/man6
install -m 644 Documentation/fceultra.6 %{buildroot}%{_mandir}/man6

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING TODO 
%doc Documentation/*.html Documentation/*.txt
%{_bindir}/fceultra
%{_mandir}/man6/fceultra.6*

%changelog
* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.98.13-0.7.pre
- rebuild for new F11 features

* Wed Jul 30 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 0.98.13-0.6.pre
- rebuild for buildsys cflags issue

* Fri Nov 02 2007  Andrea Musuruane <musuruan@gmail.com> 0.98.13-0.5.pre
- Changed license due to new guidelines.
- Removed %%{?dist} tag from changelog.

* Thu Mar 01 2007 Andrea Musuruane <musuruan@gmail.com> 0.98.13-0.4.pre
- Renamed binary from fceu to fceultra to avoid conflicts (Dribble #77).

* Tue Oct 24 2006 Andrea Musuruane <musuruan@gmail.com> 0.98.13-0.3.pre
- Added missing libGLU-devel to BuildRequires.

* Sat Oct 21 2006 Andrea Musuruane <musuruan@gmail.com> 0.98.13-0.2.pre
- Fixed Source tag URL.
- Restored name to fceultra upon requests from Dribble.
- Added a patch from Hans to fix compile on non x86.

* Sat Oct 21 2006 Andrea Musuruane <musuruan@gmail.com> 0.98.13-0.1.pre
- First release for Dribble.
- Changed name to fceu to match upstream tarball name.
- Fixed Release to meet Fedora guidelines.
- Fixed License tag.
- Fixed Group tag.
- Updated URL and Source tags.
- Fixed Buildroot to meet Fedora guidelines.
- Deleted not required dependences in BuildRequires.
- Fixed src/drivers/sexyal/convert.inc file permissions.
- No longer using old fceu-sdl name for exec file.
- Added patch from Debian to fix man entry.
- Added patch to save cheats to file (Gentoo #109359).
- Added %%{?_smp_mflags} to make invocation to speed up SMP builds.
- Avoided including man in %%doc.

* Fri Feb 18 2005 Winston Chang <winston@stdout.org>
- Updated to 0.98.13.

* Wed Dec  3 2003 Axel Thimm <Axel.Thimm@physik.fu-berlin.de>
- Updated to 0.97.5.

* Fri Jun 13 2003 Axel Thimm <Axel.Thimm@physik.fu-berlin.de> 
- Initial build.


