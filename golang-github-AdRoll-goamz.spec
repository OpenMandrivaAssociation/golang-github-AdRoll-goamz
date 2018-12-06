# list of provided golang packages
%global provided_packages    aws cloudfront s3 testutil
# https://github.com/AdRoll/goamz
%global goipath         github.com/AdRoll/goamz
%global commit          2731d20f46f42449a49b3464271c5fba8da60ed6

%gometa

Name:           golang-github-AdRoll-goamz
Version:        0
Release:        0.17%{?dist}
Summary:        Fork of the GOAMZ with additional functionality with DynamoDB
License:        LGPLv3
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.lock
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(gopkg.in/check.v1)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%forgesetup
# remove unused source code
rm -rf $(ls -d */ | egrep -v "$(echo %{provided_packages} | sed "s/  */ /g" | sed "s/ /|/g")")
cp %{SOURCE1} %{SOURCE2} .

%install
%goinstall glide.lock glide.yaml

%check
%gochecks -d s3

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc TODO.md README.md

%changelog
* Sun Nov 11 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.8.20181111git2731d20
- Bump to commit 2731d20f46f42449a49b3464271c5fba8da60ed6

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.16.20151129gitaa6e716
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.gitaa6e716
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 08 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.14.20151129gitaa6e716
- Upload glide.lock and glide.yaml

* Mon Mar 05 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.13.20151129gitaa6e716
- Update to spec 3.0

* Mon Feb 26 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.12.20151129gitaa6e716
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.gitaa6e716
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.gitaa6e716
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.gitaa6e716
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.gitaa6e716
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 09 2016 jchaloup <jchaloup@redhat.com> - 0-0.7.gitaa6e716
- Enable devel and unit-test for epel7
  related: #1269571

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.gitaa6e716
- https://fedoraproject.org/wiki/Changes/golang1.7

* Sat Mar 05 2016 jchaloup <jchaloup@redhat.com> - 0-0.5.gitaa6e716
- Bump to upstream aa6e716d710a0c7941cb2075cfbb9661f16d21f1
  related: #1269571

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.gitf8c4952
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.gitf8c4952
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 07 2015 jchaloup <jchaloup@redhat.com> - 0-0.2.gitf8c4952
- Add s3 package for openshift/origin
  resolves: #1269571

* Mon Sep 14 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.gitf8c4952
- First package for Fedora
  resolves: #1262714
