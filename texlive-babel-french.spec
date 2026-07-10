%global tl_name babel-french
%global tl_revision 79302

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Babel contributed support for French
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/french
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-french.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-french.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-french.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Requires:	texlive(carlisle)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides support for the French language for the babel
multilingual system.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/generic
%dir %{_datadir}/texmf-dist/source/generic
%dir %{_datadir}/texmf-dist/tex/generic
%dir %{_datadir}/texmf-dist/doc/generic/babel-french
%dir %{_datadir}/texmf-dist/source/generic/babel-french
%dir %{_datadir}/texmf-dist/tex/generic/babel-french
%doc %{_datadir}/texmf-dist/doc/generic/babel-french/README.md
%doc %{_datadir}/texmf-dist/doc/generic/babel-french/frenchb-fr.ltx
%doc %{_datadir}/texmf-dist/doc/generic/babel-french/frenchb-fr.pdf
%doc %{_datadir}/texmf-dist/doc/generic/babel-french/frenchb.pdf
%doc %{_datadir}/texmf-dist/doc/generic/babel-french/frenchb3-fr.ltx
%doc %{_datadir}/texmf-dist/doc/generic/babel-french/frenchb3-fr.pdf
%doc %{_datadir}/texmf-dist/doc/generic/babel-french/frenchb3.pdf
%doc %{_datadir}/texmf-dist/source/generic/babel-french/frenchb.dtx
%doc %{_datadir}/texmf-dist/source/generic/babel-french/frenchb3.dtx
%{_datadir}/texmf-dist/tex/generic/babel-french/french.ldf
%{_datadir}/texmf-dist/tex/generic/babel-french/french3.ldf
%{_datadir}/texmf-dist/tex/generic/babel-french/frenchb.lua
