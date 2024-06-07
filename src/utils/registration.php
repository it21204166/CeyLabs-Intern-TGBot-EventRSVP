<?php

function registerUser($name, $email, $num_tickets) {
    $database = json_decode(file_get_contents(__DIR__ . '/../database.json'), true);
    $userId = count($database) + 1;
    $database[] = [
        'id' => $userId,
        'name' => $name,
        'email' => $email,
        'num_tickets' => $num_tickets,
        'ticket_id' => uniqid('ticket_', true)
    ];
    file_put_contents(__DIR__ . '/../database.json', json_encode($database));
    return $userId;
}
