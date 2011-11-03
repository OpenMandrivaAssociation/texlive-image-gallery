# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/image-gallery
# catalog-date 2008-08-19 23:32:24 +0200
# catalog-license lppl
# catalog-version v1.0j
Name:		texlive-image-gallery
Version:	v1.0j
Release:	1
Summary:	Create an overview of pictures from a digital camera or from other sources
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/image-gallery
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/image-gallery.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/image-gallery.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The class may be used to create an overview of pictures from a
digital camera or from other sources. It is possible to adjust
the size of the pictures and all the margins. The example file
shows the usage.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/image-gallery/image-gallery.cls
%doc %{_texmfdistdir}/doc/latex/image-gallery/README
%doc %{_texmfdistdir}/doc/latex/image-gallery/gallery-example.pdf
%doc %{_texmfdistdir}/doc/latex/image-gallery/gallery-example.tex
%doc %{_texmfdistdir}/doc/latex/image-gallery/mypics.txt
%doc %{_texmfdistdir}/doc/latex/image-gallery/pic001.jpg
%doc %{_texmfdistdir}/doc/latex/image-gallery/pic002.jpg
%doc %{_texmfdistdir}/doc/latex/image-gallery/pic003.jpg
%doc %{_texmfdistdir}/doc/latex/image-gallery/pic004.jpg
%doc %{_texmfdistdir}/doc/latex/image-gallery/pic005.jpg
%doc %{_texmfdistdir}/doc/latex/image-gallery/pic006.jpg
%doc %{_texmfdistdir}/doc/latex/image-gallery/pic007.jpg
%doc %{_texmfdistdir}/doc/latex/image-gallery/pic008.jpg
%doc %{_texmfdistdir}/doc/latex/image-gallery/pic009.jpg
%doc %{_texmfdistdir}/doc/latex/image-gallery/pic010.jpg
%doc %{_texmfdistdir}/doc/latex/image-gallery/pic011.jpg
%doc %{_texmfdistdir}/doc/latex/image-gallery/pic012.jpg
%doc %{_texmfdistdir}/doc/latex/image-gallery/pic013.jpg
%doc %{_texmfdistdir}/doc/latex/image-gallery/pic014.jpg
%doc %{_texmfdistdir}/doc/latex/image-gallery/pic015.jpg
%doc %{_texmfdistdir}/doc/latex/image-gallery/pic016.jpg
%doc %{_texmfdistdir}/doc/latex/image-gallery/pic017.jpg
%doc %{_texmfdistdir}/doc/latex/image-gallery/pic018.jpg
%doc %{_texmfdistdir}/doc/latex/image-gallery/pic019.jpg
%doc %{_texmfdistdir}/doc/latex/image-gallery/pic020.jpg
%doc %{_texmfdistdir}/doc/latex/image-gallery/pic021.jpg
%doc %{_texmfdistdir}/doc/latex/image-gallery/pic022.jpg
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
