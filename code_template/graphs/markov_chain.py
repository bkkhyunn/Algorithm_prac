import numpy as np

class MarkovChain:
    def __init__(self, transition_matrix, states):
        # 상태 전이 행렬
        self.transition_matrix = np.array(transition_matrix)
        self.states = states
        self.num_states = len(states)

    # step 별 상태를 기록하는 함수
    def generate_sequence(self, start_state, steps):
        state_sequence = [start_state]
        current_state = start_state

        for _ in range(steps):
            next_state = np.random.choice(self.states, p=self.transition_matrix[self.states.index(current_state)])
            state_sequence.append(next_state)
            current_state = next_state

        return state_sequence

    # 특정 step 의 상태를 출력하는 함수
    def transition_at_step(self, start_state, steps):
        current_state = start_state

        for _ in range(steps):
            current_state = np.random.choice(self.states, p=self.transition_matrix[self.states.index(current_state)])

        return current_state

    # 특정 step 후 특정 상태의 확률을 출력하는 함수
    def probability_of_state_after_steps(self, start_state, target_state, steps):
        current_state = start_state
        state_index = self.states.index(target_state)
        
        for _ in range(steps):
            current_state = np.random.choice(self.states, p=self.transition_matrix[self.states.index(current_state)])

        return self.transition_matrix[self.states.index(current_state), state_index]

# 예제
if __name__ == "__main__":

    states = ['Sunny', 'Rainy', 'Cloudy']
    transition_matrix = [
        [0.7, 0.2, 0.1],
        [0.1, 0.6, 0.3],
        [0.2, 0.5, 0.3]
    ]

    mc = MarkovChain(transition_matrix, states)

    start_state = 'Sunny' # 오늘 날씨

    # 오늘이 Sunny 일 때 5일 동안의 날씨 확률
    steps = 5
    sequence = mc.generate_sequence(start_state, steps)
    print(f"오늘 상태가 {start_state} 일 때 {steps} 동안의 날씨 확률")
    print(sequence)

    # 오늘이 Sunny 일 때 3일 후의 날씨
    steps = 3
    final_state = mc.transition_at_step(start_state, steps)
    print(f"{steps}일 후 날씨는 {final_state}")

    # 오늘이 Sunny 일 때 2일 후에 Cloudy 일 확률
    target_state = 'Cloudy'
    steps = 2
    probability = mc.probability_of_state_after_steps(start_state, target_state, steps)
    print(f"{steps}일 후에 {target_state} 일 확률은 {probability:.4f}")