#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-guard-compat
Version  : 1.2.1
Release  : 7
URL      : https://rubygems.org/downloads/guard-compat-1.2.1.gem
Source0  : https://rubygems.org/downloads/guard-compat-1.2.1.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-devise
BuildRequires : rubygem-diff-lcs
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-rspec-expectations
BuildRequires : rubygem-rspec-mocks
BuildRequires : rubygem-rspec-support
BuildRequires : rubygem-rubygems-tasks

%description
# Guard::Compat
Currently, provides only a test helper for testing custom Guard plugins.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n guard-compat-1.2.1
gem spec %{SOURCE0} -l --ruby > rubygem-guard-compat.gemspec

%build
gem build rubygem-guard-compat.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
guard-compat-1.2.1.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/guard-compat-1.2.1
rspec -I.:lib spec/
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/guard-compat-1.2.1.gem
/usr/lib64/ruby/gems/2.3.0/gems/guard-compat-1.2.1/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/guard-compat-1.2.1/.rspec
/usr/lib64/ruby/gems/2.3.0/gems/guard-compat-1.2.1/.rubocop.yml
/usr/lib64/ruby/gems/2.3.0/gems/guard-compat-1.2.1/.rubocop_todo.yml
/usr/lib64/ruby/gems/2.3.0/gems/guard-compat-1.2.1/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/guard-compat-1.2.1/LICENSE.txt
/usr/lib64/ruby/gems/2.3.0/gems/guard-compat-1.2.1/README.md
/usr/lib64/ruby/gems/2.3.0/gems/guard-compat-1.2.1/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/guard-compat-1.2.1/guard-compat.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/guard-compat-1.2.1/lib/guard/compat.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-compat-1.2.1/lib/guard/compat/example.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-compat-1.2.1/lib/guard/compat/plugin.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-compat-1.2.1/lib/guard/compat/test/helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-compat-1.2.1/lib/guard/compat/test/template.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-compat-1.2.1/lib/guard/compat/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-compat-1.2.1/spec/guard/compat/example_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-compat-1.2.1/spec/guard/compat/example_template_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-compat-1.2.1/spec/guard/compat/no_guard_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/guard-compat-1.2.1/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.3.0/specifications/guard-compat-1.2.1.gemspec
