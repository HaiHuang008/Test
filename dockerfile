# build sdk docker image
FROM ubuntu:16.04
MAINTAINER YoungHuang

RUN apt-get update && apt-get install -y \
            apt-utils \
            iputils-ping \
            net-tools \
            vim \
            curl \
            wget \
            make \
            gcc \
            g++ \
            subversion \
            python-pip \
            bzip2 \
            python-yaml \
            autoconf \
            automake \
            libtool \
            bison \
            flex \
        && python -m pip install filelock==3.1.0 && \
           python -m pip install pyyaml && \
           rm -rf /var/lib/apt/lists/* && \
           rm -rf /var/cache/apk/* && \
           apt-get remove -y python-pip && \
           apt-get autoremove -y

RUN perl -MCPAN -e install Spiffy &&  cpan install \
                  Data::Compare \
                  Hash::Merge \
                  Moose \
                  YAML \
                  YAML::Any \
                  YAML::XS \
                  List::MoreUtils \
                  namespace::autoclean

# install gcc-7.5.0
RUN mkdir /home/gcc-tool && \
           mkdir /home/gcc-tool/gcc-build-7.5.0 && \
           wget -P /home/gcc-tool/ https://mirrors.ustc.edu.cn/gnu/gcc/gcc-7.5.0/gcc-7.5.0.tar.gz && \
           wget -P /home/gcc-tool/ https://mirrors.ustc.edu.cn/gnu/gmp/gmp-6.1.0.tar.bz2 && \
           wget -P /home/gcc-tool/ https://mirrors.ustc.edu.cn/gnu/mpc/mpc-1.0.3.tar.gz  && \
           wget -P /home/gcc-tool/ https://mirrors.ustc.edu.cn/gnu/mpfr/mpfr-3.1.4.tar.bz2 && \
           wget -P /home/gcc-tool/ http://ftp.ntua.gr/mirror/gnu/gcc/infrastructure/isl-0.16.1.tar.bz2 && \
           tar -C /home/gcc-tool/ -xvf /home/gcc-tool/gcc-7.5.0.tar.gz && \
           mv /home/gcc-tool/gmp-6.1.0.tar.bz2  /home/gcc-tool/gcc-7.5.0 && \
           mv /home/gcc-tool/mpc-1.0.3.tar.gz  /home/gcc-tool/gcc-7.5.0 && \
           mv /home/gcc-tool/mpfr-3.1.4.tar.bz2 /home/gcc-tool/gcc-7.5.0 && \
           mv /home/gcc-tool/isl-0.16.1.tar.bz2 /home/gcc-tool/gcc-7.5.0 && \
           cd  /home/gcc-tool/gcc-7.5.0/ && \
           ./contrib/download_prerequisites && \
           cd /home/gcc-tool/gcc-build-7.5.0 && \
           /home/gcc-tool/gcc-7.5.0/configure --enable-checking=release --enable-languages=c,c++ --disable-multilib && \
           make -j8 && \
           make install && \
           rm -rf /home/gcc-tool/
           
           
