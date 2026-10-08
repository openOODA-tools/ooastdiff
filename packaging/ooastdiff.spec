Name:           ooastdiff
Version:        0.2.0
Release:        1%{?dist}
Summary:        Programming language AST differ ignoring cosmetic whitespace and comment changes.
License:        Apache-2.0
URL:            https://github.com/openOODA-tools/ooastdiff
Source0:        ooastdiff-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooastdiff is a sovereign, capability-bounded AST & SYNTAX DIFFER written
in pure openOODA, featuring zero ambient authority, semantic token
differencing ignoring cosmetic whitespace, and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooastdiff
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooastdiff-uninstall

%files
/usr/bin/ooastdiff
/usr/bin/ooastdiff-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.2.0-1
- Elevate to v0.2.0 with AST differ, token Myers LCS algorithm, and MCP server
