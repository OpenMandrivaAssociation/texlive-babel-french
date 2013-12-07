# revision 32256
# category Package
# catalog-ctan /macros/latex/contrib/babel-contrib/french
# catalog-date 2013-11-27 17:50:38 +0100
# catalog-license lppl1.3
# catalog-version 2.6f
Name:		texlive-babel-french
Version:	2.6f
Release:	5
Summary:	Babel contributed support for French
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/french
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-french.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-french.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-french.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package establishes French conventions in a document (or a
subset of the conventions, if French is not the main language
of the document).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/babel-french/frenchb.ldf
%doc %{_texmfdistdir}/doc/generic/babel-french/frenchb.pdf
#- source
%doc %{_texmfdistdir}/source/generic/babel-french/frenchb.dtx
%doc %{_texmfdistdir}/source/generic/babel-french/frenchb.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
