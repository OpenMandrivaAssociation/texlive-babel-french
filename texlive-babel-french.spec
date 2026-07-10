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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(carlisle)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides support for the French language for the babel
multilingual system.

