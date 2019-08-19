#include <bits/stdc++.h>
#include <tcframe/spec.hpp>
using namespace std;
using namespace tcframe;

typedef long long ll;

class ProblemSpec : public BaseProblemSpec {
protected:
    const int maxT = 100;
    const int maxN = (int)1e7;

    int T;
    int N;

    long long ans;

    void MultipleTestCasesConfig() {
        Counter(T);
        OutputPrefix("Case #%d: ");
    }

    void InputFormat(){
        LINE(N);
    }

    void OutputFormat(){
        LINE(ans);
    }

    void GradingConfig(){
        TimeLimit(1);
        MemoryLimit(64);
    }

    void MultipleTestCasesConstraints(){
        CONS(1 <= T && T <= maxT);
    }

    void Constraints(){
        CONS(1 <= N && N <= maxN);
    }

private:
    // none
};

class TestSpec : public BaseTestSpec<ProblemSpec> {
protected:
    void SampleTestCase1(){
        Input({ "1" });
        Output({ "1" });
    }
    void SampleTestCase2(){
        Input({ "2" });
        Output({ "8" });
    }
    void SampleTestCase3(){
        Input({ "10" });
        Output({ "346789" });
    }

    void TestGroup1(){
        CASE(N = 1);
        CASE(N = 2);
        CASE(N = 10);
    }

    void TestGroup2(){
        int t = rnd.nextInt(5, maxT);
        for (int i=1; i<=t; i++) {
            CASE(N = rnd.nextInt(1, maxN));
        }
    }
    void TestGroup3(){
        int t = rnd.nextInt(5, maxT);
        for (int i=1; i<=t; i++) {
            CASE(N = rnd.nextInt(1, maxN));
        }
    }
    void TestGroup4(){
        int t = rnd.nextInt(5, maxT);
        for (int i=1; i<=t; i++) {
            CASE(N = rnd.nextInt(1, maxN));
        }
    }

    void TestGroup5(){
        int t = rnd.nextInt(10, maxT);
        for (int i=1; i<=t; i++) {
            CASE(N = rnd.nextInt(maxN/10, maxN));
        }
    }
    void TestGroup6(){
        int t = rnd.nextInt(10, maxT);
        for (int i=1; i<=t; i++) {
            CASE(N = rnd.nextInt(maxN/10, maxN));
        }
    }

    void TestGroup7(){
        int t = rnd.nextInt(10, maxT);
        for (int i=1; i<=t; i++) {
            CASE(N = rnd.nextInt(maxN/2, maxN));
        }
    }
    void TestGroup8(){
        int t = rnd.nextInt(10, maxT);
        for (int i=1; i<=t; i++) {
            CASE(N = rnd.nextInt(maxN/2, maxN));
        }
    }

    void TestGroup9(){
        int t = maxT;
        for (int i=1; i<=t; i++) {
            CASE(N = rnd.nextInt(maxN/2, maxN));
        }
    }

    void TestGroup10(){
        int t = maxT;
        for (int i=1; i<=t; i++) {
            CASE(N = rnd.nextInt(9*maxN/10, maxN));
        }
    }

    void TestGroup11(){
        for (int i=1000002; i<=maxN; i+=1000003) {
            CASE(N = i);
        }
    }

private:
    //none
};
