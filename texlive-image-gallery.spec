Name:		texlive-image-gallery
Version:	15878
Release:	2
Summary:	Create an overview of pictures from a digital camera or from other sources
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/image-gallery
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/image-gallery.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/image-gallery.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class may be used to create an overview of pictures from a
digital camera or from other sources. It is possible to adjust
the size of the pictures and all the margins. The example file
shows the usage.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
