#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-guard-compat
Version  : 1.2.1
Release  : 4
URL      : https://rubygems.org/downloads/guard-compat-1.2.1.gem
Source0  : https://rubygems.org/downloads/guard-compat-1.2.1.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
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
rspec -Ilib spec/
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/guard-compat-1.2.1.gem
/usr/lib64/ruby/gems/2.2.0/doc/guard-compat-1.2.1/ri/Guard/Compat/Test/Template/Session/GlobalWatchesNotImplemented/cdesc-GlobalWatchesNotImplemented.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-compat-1.2.1/ri/Guard/Compat/Test/Template/Session/GlobalWatchesNotImplemented/message-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-compat-1.2.1/ri/Guard/Compat/Test/Template/Session/MultipleGuardNotImplemented/cdesc-MultipleGuardNotImplemented.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-compat-1.2.1/ri/Guard/Compat/Test/Template/Session/MultipleGuardNotImplemented/message-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-compat-1.2.1/ri/Guard/Compat/Test/Template/Session/_watches-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-compat-1.2.1/ri/Guard/Compat/Test/Template/Session/cdesc-Session.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-compat-1.2.1/ri/Guard/Compat/Test/Template/Session/guard-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-compat-1.2.1/ri/Guard/Compat/Test/Template/Session/match-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-compat-1.2.1/ri/Guard/Compat/Test/Template/Session/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-compat-1.2.1/ri/Guard/Compat/Test/Template/Session/watch-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-compat-1.2.1/ri/Guard/Compat/Test/Template/cdesc-Template.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-compat-1.2.1/ri/Guard/Compat/Test/Template/changed-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-compat-1.2.1/ri/Guard/Compat/Test/Template/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-compat-1.2.1/ri/Guard/Compat/Test/cdesc-Test.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-compat-1.2.1/ri/Guard/Compat/UI/cdesc-UI.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-compat-1.2.1/ri/Guard/Compat/UI/color-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-compat-1.2.1/ri/Guard/Compat/UI/color_enabled%3f-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-compat-1.2.1/ri/Guard/Compat/UI/debug-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-compat-1.2.1/ri/Guard/Compat/UI/deprecation-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-compat-1.2.1/ri/Guard/Compat/UI/error-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-compat-1.2.1/ri/Guard/Compat/UI/info-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-compat-1.2.1/ri/Guard/Compat/UI/notify-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-compat-1.2.1/ri/Guard/Compat/UI/warning-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-compat-1.2.1/ri/Guard/Compat/cdesc-Compat.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-compat-1.2.1/ri/Guard/Compat/matching_files-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-compat-1.2.1/ri/Guard/Compat/watched_directories-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-compat-1.2.1/ri/Guard/MyPlugin/cdesc-MyPlugin.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-compat-1.2.1/ri/Guard/MyPlugin/run_all-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-compat-1.2.1/ri/Guard/MyPlugin/run_on_modifications-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-compat-1.2.1/ri/Guard/MyPlugin/start-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-compat-1.2.1/ri/Guard/Notifier/cdesc-Notifier.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-compat-1.2.1/ri/Guard/Plugin/cdesc-Plugin.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-compat-1.2.1/ri/Guard/Plugin/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-compat-1.2.1/ri/Guard/Plugin/options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-compat-1.2.1/ri/Guard/UI/cdesc-UI.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-compat-1.2.1/ri/Guard/cdesc-Guard.ri
/usr/lib64/ruby/gems/2.2.0/doc/guard-compat-1.2.1/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/gems/guard-compat-1.2.1/.gitignore
/usr/lib64/ruby/gems/2.2.0/gems/guard-compat-1.2.1/.rspec
/usr/lib64/ruby/gems/2.2.0/gems/guard-compat-1.2.1/.rubocop.yml
/usr/lib64/ruby/gems/2.2.0/gems/guard-compat-1.2.1/.rubocop_todo.yml
/usr/lib64/ruby/gems/2.2.0/gems/guard-compat-1.2.1/Gemfile
/usr/lib64/ruby/gems/2.2.0/gems/guard-compat-1.2.1/LICENSE.txt
/usr/lib64/ruby/gems/2.2.0/gems/guard-compat-1.2.1/README.md
/usr/lib64/ruby/gems/2.2.0/gems/guard-compat-1.2.1/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/guard-compat-1.2.1/guard-compat.gemspec
/usr/lib64/ruby/gems/2.2.0/gems/guard-compat-1.2.1/lib/guard/compat.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-compat-1.2.1/lib/guard/compat/example.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-compat-1.2.1/lib/guard/compat/plugin.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-compat-1.2.1/lib/guard/compat/test/helper.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-compat-1.2.1/lib/guard/compat/test/template.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-compat-1.2.1/lib/guard/compat/version.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-compat-1.2.1/spec/guard/compat/example_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-compat-1.2.1/spec/guard/compat/example_template_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-compat-1.2.1/spec/guard/compat/no_guard_spec.rb
/usr/lib64/ruby/gems/2.2.0/gems/guard-compat-1.2.1/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.2.0/specifications/guard-compat-1.2.1.gemspec
