from reduced_residue_system import reduced_residue_system_primorial_two_classification

for i in range(1, 20):
    two_classification = reduced_residue_system_primorial_two_classification(i)
    print(i, two_classification.composite_to_composite,
          two_classification.composite_to_prime,
          two_classification.prime_to_composite,
          two_classification.prime_to_prime)
