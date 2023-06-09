import subprocess

def computeTasas(path):
    wer_command = ['./tasas/tasas', '-f', "#", '-s', " ", "-ie", path]
    cer_command = ['./tasas/tasas', '-f', "#", "-ie", path]

    wer = float(subprocess.check_output(wer_command).strip())
    cer = float(subprocess.check_output(cer_command).strip())

    ci_wer_command = ['./tasas/tasasIntervalo', '-f', "#", '-s', " ", "-ie", path]
    ci_cer_command = ['./tasas/tasasIntervalo', '-f', "#", "-ie", path]

    ci_wer = float(subprocess.check_output(ci_wer_command).decode('utf-8').split('+-')[1].strip())
    ci_cer = float(subprocess.check_output(ci_cer_command).decode('utf-8').split('+-')[1].strip())

    return wer, cer, ci_wer, ci_cer
