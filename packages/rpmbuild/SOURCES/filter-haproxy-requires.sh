#!/bin/sh
/usr/lib/rpm/perl.req $* |
sed -e '/perl(IO::Socket::PortState)/d' |
sed -e '/perl(Net::Server::PreFork)/d' 


