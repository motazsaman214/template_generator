import os
import argparse

def create_problem_structure(path, problem_name):
    """
    Creates a folder structure for a coding problem, including a .cpp file with initial content,
    and empty input.txt and output.txt files.

    Args:
    path (str): The base path where the problem folder will be created.
    problem_name (str): The name of the problem, used for folder and file naming.
    """
    # Create the folder with the name of the problem
    problem_folder = os.path.join(path, problem_name)
    os.makedirs(problem_folder, exist_ok=True)

    # Create the .cpp file with the initial content
    cpp_file_path = os.path.join(problem_folder, f"{problem_name}.cpp")
    with open(cpp_file_path, 'w') as cpp_file:
        cpp_content = '''#include <bits/stdc++.h>
using namespace std;
#define ll long long

void fastIO(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

void fileIO(void) {
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
}

void solve() {
    // Problem-specific solution goes here
}

int main(){
    fastIO();fileIO();
    int t = 1; cin >> t;
    while(t--){
        solve();
        /*cout << solve() << endl;*/
        /*if(solve())
            cout << "YES\\n";
        else
            cout << "NO\\n";*/
        /*cout << "Case #" << i << ": ";*/
        /*cout << "Case #" << i << ": " << (solve() ? "YES" : "NO") << endl;*/
    }
    return 0;
}'''
        cpp_file.write(cpp_content)

    # Create empty input.txt and output.txt files
    input_file_path = os.path.join(problem_folder, "input.txt")
    output_file_path = os.path.join(problem_folder, "output.txt")
    open(input_file_path, 'w').close()  # Create empty input file
    open(output_file_path, 'w').close()  # Create empty output file

    print(f"Problem folder '{problem_name}' and files created successfully at: {problem_folder}")

if __name__ == "__main__":
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Create a folder and generate files for a coding problem")
    parser.add_argument("path", type=str, help="The path where the folder will be created")
    parser.add_argument("problem_name", type=str, help="The name of the problem")
    parser.add_argument("--add-code", action="store_true", help="Automatically add default content to the .cpp file")
    args = parser.parse_args()

    # Call the function with the provided arguments
    create_problem_structure(args.path, args.problem_name)
