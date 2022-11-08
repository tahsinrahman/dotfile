if status is-interactive
    # Commands to run in interactive sessions can go here
end

fundle plugin 'IlanCosman/tide' --url 'git@github.com:IlanCosman/tide#tags/v5.5.1'
fundle plugin 'jethrokuan/z'
fundle plugin 'PatrickF1/fzf.fish'
fundle plugin 'franciscolourenco/done'
fundle plugin 'jorgebucaran/replay.fish'
fundle plugin 'jorgebucaran/autopair.fish'
fundle plugin joseluisq/gitnow --url 'git@github.com:joseluisq/gitnow.git#tags/2.10.0'
fundle plugin 'gazorby/fish-abbreviation-tips'
fundle plugin 'tuvistavie/oh-my-fish-core'
fundle plugin 'edc/bass'

fundle init

# direnv hook fish | source

fish_add_path $HOME/.spicetify
