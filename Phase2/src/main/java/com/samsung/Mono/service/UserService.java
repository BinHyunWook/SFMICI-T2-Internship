package com.samsung.Mono.service;

import com.samsung.Mono.data.UserJpaRepository;
import com.samsung.Mono.entity.User;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@RequiredArgsConstructor
@Service
public class UserService {

    private final UserJpaRepository userJpaRepository;

    public User register(User user){
        return userJpaRepository.save(user);
    }


}
