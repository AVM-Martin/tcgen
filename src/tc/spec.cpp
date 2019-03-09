#include <bits/stdc++.h>
#include <tcframe/spec.hpp>
using namespace std;
using namespace tcframe;

class ProblemSpec : public BaseProblemSpec {
protected:
    int A, B;
    int Res;

    void InputFormat(){
        LINE(A, B);
    }

    void OutputFormat(){
        LINE(Res);
    }

    void GradingConfig(){
        TimeLimit(1);
        MemoryLimit(64);
    }

    void Constraints(){
        CONS(1 <= A && A <= 10);
        CONS(1 <= B && B <= 10);
    }

private:
    // none
};

class TestSpec : public BaseTestSpec<ProblemSpec> {
protected:
    void SampleTestCase1(){
        Input({ "1 2" });
        Output({ "3" });
    }

    void TestCases(){
        for(int i=1; i<=10; i++) CASE(A = rnd.nextInt(1,10), B = rnd.nextInt(1,10));
    }

private:
    // none
};
