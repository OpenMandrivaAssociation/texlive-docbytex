Name:		texlive-docbytex
Version:	34294
Release:	2
Summary:	Creating documentation from source code
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/docbytex
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/docbytex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/docbytex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package creates documentation from C source code, or other
programming languages.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/docbytex/docby.tex
%doc %{_texmfdistdir}/doc/generic/docbytex/README
%doc %{_texmfdistdir}/doc/generic/docbytex/annonce
%doc %{_texmfdistdir}/doc/generic/docbytex/base.c
%doc %{_texmfdistdir}/doc/generic/docbytex/base.d
%doc %{_texmfdistdir}/doc/generic/docbytex/cosi.c
%doc %{_texmfdistdir}/doc/generic/docbytex/docby-e.d
%doc %{_texmfdistdir}/doc/generic/docbytex/docby-e.pdf
%doc %{_texmfdistdir}/doc/generic/docbytex/docby.d
%doc %{_texmfdistdir}/doc/generic/docbytex/docby.pdf
%doc %{_texmfdistdir}/doc/generic/docbytex/lup.pdf
%doc %{_texmfdistdir}/doc/generic/docbytex/lup.tex
%doc %{_texmfdistdir}/doc/generic/docbytex/main.c
%doc %{_texmfdistdir}/doc/generic/docbytex/main.d
%doc %{_texmfdistdir}/doc/generic/docbytex/win.c
%doc %{_texmfdistdir}/doc/generic/docbytex/win.d

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
