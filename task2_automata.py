# Clean Python State Machines and Graphical Configurations
import os
from graphviz import Digraph

def generate_visualizations():
    # Password Verification DFA
    pwd_dfa = Digraph('Password_DFA', comment='Password Verification DFA')
    pwd_dfa.attr(rankdir='LR', size='8,5')
    pwd_dfa.node('q_dead', 'q_dead', shape='circle')
    pwd_dfa.node('q0', 'q0', shape='circle')
    pwd_dfa.node('q1', 'q1', shape='circle')
    pwd_dfa.node('q2', 'q2', shape='circle')
    pwd_dfa.node('q3', 'q3', shape='circle')
    pwd_dfa.node('q4', 'q4', shape='doublecircle')

    pwd_dfa.edge('q0', 'q1', label='[A-Z]')
    pwd_dfa.edge('q0', 'q_dead', label='[^A-Z]')
    pwd_dfa.edge('q1', 'q2', label='[a-z]')
    pwd_dfa.edge('q1', 'q_dead', label='[^a-z]')
    pwd_dfa.edge('q2', 'q3', label='[a-z]')
    pwd_dfa.edge('q2', 'q_dead', label='[^a-z]')
    pwd_dfa.edge('q3', 'q4', label='[0-9]')
    pwd_dfa.edge('q3', 'q_dead', label='[^0-9]')
    pwd_dfa.edge('q4', 'q_dead', label='any char')
    pwd_dfa.edge('q_dead', 'q_dead', label='any char')
    pwd_dfa.render('password_dfa', format='png', cleanup=True)

    # Email Validator DFA
    email_dfa = Digraph('Email_DFA', comment='Email Validator DFA')
    email_dfa.attr(rankdir='LR', size='10,5')
    email_dfa.node('q_dead', 'q_dead', shape='circle')
    for i in range(8):
        shape = 'doublecircle' if i == 7 else 'circle'
        email_dfa.node(f'q{i}', f'q{i}', shape=shape)

    email_dfa.edge('q0', 'q1', label='[a-zA-Z0-9]')
    email_dfa.edge('q0', 'q_dead', label='[^a-zA-Z0-9]')
    email_dfa.edge('q1', 'q1', label='[a-zA-Z0-9]')
    email_dfa.edge('q1', 'q2', label='@')
    email_dfa.edge('q1', 'q_dead', label='[^a-zA-Z0-9, @]')
    email_dfa.edge('q2', 'q3', label='[a-zA-Z0-9]')
    email_dfa.edge('q2', 'q_dead', label='[^a-zA-Z0-9]')
    email_dfa.edge('q3', 'q3', label='[a-zA-Z0-9]')
    email_dfa.edge('q3', 'q4', label='.')
    email_dfa.edge('q3', 'q_dead', label='[^a-zA-Z0-9, .]')
    email_dfa.edge('q4', 'q5', label='c')
    email_dfa.edge('q4', 'q_dead', label='^c')
    email_dfa.edge('q5', 'q6', label='o')
    email_dfa.edge('q5', 'q_dead', label='^o')
    email_dfa.edge('q6', 'q7', label='m')
    email_dfa.edge('q6', 'q_dead', label='^m')
    email_dfa.edge('q7', 'q_dead', label='any char')
    email_dfa.edge('q_dead', 'q_dead', label='any char')
    email_dfa.render('email_dfa', format='png', cleanup=True)

    # ATM PIN Verification DFA
    atm_dfa = Digraph('ATM_DFA', comment='ATM PIN Verification DFA')
    atm_dfa.attr(rankdir='LR', size='8,5')
    atm_dfa.node('q_start', 'Start/Attempt1', shape='circle')
    atm_dfa.node('q_att2', 'Attempt2', shape='circle')
    atm_dfa.node('q_att3', 'Attempt3', shape='circle')
    atm_dfa.node('q_unlocked', 'Unlocked', shape='doublecircle')
    atm_dfa.node('q_blocked', 'Blocked', shape='circle')

    atm_dfa.edge('q_start', 'q_unlocked', label='Correct PIN')
    atm_dfa.edge('q_start', 'q_att2', label='Incorrect PIN')
    atm_dfa.edge('q_att2', 'q_unlocked', label='Correct PIN')
    atm_dfa.edge('q_att2', 'q_att3', label='Incorrect PIN')
    atm_dfa.edge('q_att3', 'q_unlocked', label='Correct PIN')
    atm_dfa.edge('q_att3', 'q_blocked', label='Incorrect PIN')
    atm_dfa.edge('q_unlocked', 'q_unlocked', label='any action')
    atm_dfa.edge('q_blocked', 'q_blocked', label='any action')
    atm_dfa.render('atm_dfa', format='png', cleanup=True)

def simulate_password(input_str: str) -> bool:
    state = 'q0'
    for char in input_str:
        if state == 'q0':
            if char.isupper(): state = 'q1'
            else: state = 'q_dead'
        elif state == 'q1':
            if char.islower(): state = 'q2'
            else: state = 'q_dead'
        elif state == 'q2':
            if char.islower(): state = 'q3'
            else: state = 'q_dead'
        elif state == 'q3':
            if char.isdigit(): state = 'q4'
            else: state = 'q_dead'
        elif state == 'q4':
            state = 'q_dead'
        elif state == 'q_dead':
            pass
    return state == 'q4'

def simulate_email(input_str: str) -> bool:
    state = 'q0'
    for char in input_str:
        if state == 'q0':
            if char.isalnum(): state = 'q1'
            else: state = 'q_dead'
        elif state == 'q1':
            if char.isalnum(): state = 'q1'
            elif char == '@': state = 'q2'
            else: state = 'q_dead'
        elif state == 'q2':
            if char.isalnum(): state = 'q3'
            else: state = 'q_dead'
        elif state == 'q3':
            if char.isalnum(): state = 'q3'
            elif char == '.': state = 'q4'
            else: state = 'q_dead'
        elif state == 'q4':
            if char == 'c': state = 'q5'
            else: state = 'q_dead'
        elif state == 'q5':
            if char == 'o': state = 'q6'
            else: state = 'q_dead'
        elif state == 'q6':
            if char == 'm': state = 'q7'
            else: state = 'q_dead'
        elif state == 'q7':
            state = 'q_dead'
        elif state == 'q_dead':
            pass
    return state == 'q7'

def simulate_atm(attempts: list) -> str:
    state = 'q_start'
    for attempt in attempts:
        if state == 'q_start':
            if attempt == 'correct': state = 'q_unlocked'
            else: state = 'q_att2'
        elif state == 'q_att2':
            if attempt == 'correct': state = 'q_unlocked'
            else: state = 'q_att3'
        elif state == 'q_att3':
            if attempt == 'correct': state = 'q_unlocked'
            else: state = 'q_blocked'
        elif state in ['q_unlocked', 'q_blocked']:
            pass
    return state