define deref_custom
    set $addr = $arg0

    if $argc >= 2
        set $depth = $arg1
    else
        set $depth = 1
    end

    while ($depth > 0)
        set $addr = *(void **)$addr
        set $depth = $depth - 1
    end

    x/s $addr
    x/x $addr
    x/w $addr
    x/d $addr
end

