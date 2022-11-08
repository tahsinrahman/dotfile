set -xg GOPATH $HOME/go
set -xg GOBIN $GOPATH/bin
set -xg EDITOR vim

# set -xg PATH /usr/local/opt/make/libexec/gnubin $PATH
# set -gx PATH /Library/TeX/texbin $PATH
set -gx PATH /opt/homebrew/bin $PATH
set -gx PATH /opt/homebrew/sbin $PATH


alias k="kubectl"
alias kp="k get pods"
alias kd="k get deploy"
alias ks="k get svc"
alias kep="k get ep"

alias kn="k neat"

alias ls='lsd'
alias ll='ls -l'
alias la='ls -a'
alias lla='ls -la'
alias lt='ls --tree --depth 2'
alias diff='delta'

alias watch='watch fish -c'

