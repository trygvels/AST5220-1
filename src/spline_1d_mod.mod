	  ')  d   k820309    Ö          15.0        (ĖV                                                                                                           
       spline_1D_mod.f90 SPLINE_1D_MOD                                                    
                                                              u #LOCATE_INT    #LOCATE_DP                                                                                                                                                                                                                                                                                                                      %         @    X                                                      #LOCATE_INT%SIZE    #XX    #X 	                                                  SIZE           
 @                                                  -             &                                                     
                                 	           %         @    X                                                     #LOCATE_DP%SIZE 
   #XX    #X                                              
     SIZE           
 @                                                 
 .             &                                                     
                                      
      #         @                                                      #SPLINE%SIZE    #X    #Y    #YP1    #YPN    #Y2                                                   SIZE           
 @                                                 
              &                                                     
                                                    
              &                                                     
                                      
                
                                      
                D @                                                 
               &                                           #         @                                                     #TRIDAG%SIZE    #A    #B    #C    #R    #U                                                   SIZE           
                                                    
 '             &                                                     
 @                                                 
 (             &                                                     
                                                    
 )             &                                                     
                                                    
 *             &                                                     D                                                   
 +              &                                           #         @                                                      #SPLINE_ELEGANT%SIZE    #X    #Y    #YP1    #YPN     #Y2 !                                                  SIZE           
 @                                                 
              &                                                     
                                                    
 	             &                                                     
                                      
                
                                       
                D @                              !                   
 
              &                                           %         @                               "                   
       #SPLINT%MIN #   #SPLINT%MAX $   #SPLINT%SIZE %   #XA &   #YA '   #Y2A (   #X )                                             #     MIN                                           $     MAX                                           %     SIZE           
 @                              &                   
              &                                                     
                                 '                   
              &                                                     
                                 (                   
              &                                                     
  @                              )     
      %         @                                *                   
       #SPLINT_DERIV%MIN +   #SPLINT_DERIV%MAX ,   #SPLINT_DERIV%SIZE -   #XA .   #YA /   #Y2A 0   #X 1                                             +     MIN                                           ,     MAX                                           -     SIZE           
 @                              .                   
              &                                                     
                                 /                   
              &                                                     
                                 0                   
              &                                                     
  @                              1     
      #         @                                   2                   #SPLINT_DERIV_ALL_NODES%SIZE 3   #XA 4   #YA 5   #Y2A 6   #DERIV 7                                             3     SIZE           
 @                              4                   
              &                                                     
                                 5                   
              &                                                     
                                 6                   
              &                                                     D                                7                   
               &                                           #         @                                   8                   #SMOOTH_SPLINE%DOT_PRODUCT 9   #SMOOTH_SPLINE%EXP :   #SMOOTH_SPLINE%PRESENT ;   #SMOOTH_SPLINE%TRIM <   #SMOOTH_SPLINE%SIZE =   #WEIGHT >   #ALPHA ?   #X @   #Y A   #YP1 B   #YPN C   #Y2 D   #VARIANCE E                                             9     DOT_PRODUCT                                           :     EXP                                           ;     PRESENT                                           <     TRIM                                           =     SIZE           
  @                              >                    1           
                                 ?     
                
 @                              @                   
              &                                                     
D                                A                   
               &                                                     
                                 B     
                
                                 C     
                D                                D                   
               &                                                     
 @                              E                   
              &                                           #         @                                   F                   #QSIMP%ABS G   #X_0 H   #Y_0 I   #Y2_0 J   #A K   #B L   #S M                                             G     ABS           
  @                              H                   
 /             & p                                                    
  @                              I                   
 0             & p                                                    
  @                              J                   
 1             & p                                                    
  @                              K     
                
  @                              L     
                D                                M     
       #         @                                  N                   #TRAPZD%REAL O   #X_0 P   #Y_0 Q   #Y2_0 R   #A S   #B T   #S U   #N V                              @              O     REAL           
  @                              P                   
 2             & p                                                    
  @                              Q                   
 3             & p                                                    
  @                              R                   
 4             & p                                                    
  @                              S     
                
  @                              T     
                
D                                U     
                 
                                 V           %         @  @                             W                   
       #ZRIDDR%SIGN X   #ZRIDDR%SQRT Y   #ZRIDDR%ABS Z   #ZRIDDR%SIZE [   #X_0 \   #Y_0 ]   #Y2_0 ^   #X1 _   #X2 `   #ZEROPT a   #XACC b                                             X     SIGN                                           Y     SQRT                                           Z     ABS                                           [     SIZE           
  @                              \                   
 5             & p                                                    
 @                              ]                   
 6             & p                                                    
  @                              ^                   
 7             & p                                                    
  @                              _     
                
  @                              `     
                
                                 a     
                
                                 b     
             (      fn#fn    Č   @   J   HEALPIX_TYPES      _       gen@LOCATE !   g  p       DP+HEALPIX_TYPES "   Ũ  p       I4B+HEALPIX_TYPES "   G  p       LGT+HEALPIX_TYPES    ·  t       LOCATE_INT     +  =      LOCATE_INT%SIZE    h     a   LOCATE_INT%XX    ô  @   a   LOCATE_INT%X    4  s       LOCATE_DP    §  =      LOCATE_DP%SIZE    ä     a   LOCATE_DP%XX    p  @   a   LOCATE_DP%X    °         SPLINE    1  =      SPLINE%SIZE    n     a   SPLINE%X    ú     a   SPLINE%Y      @   a   SPLINE%YP1    Æ  @   a   SPLINE%YPN         a   SPLINE%Y2      |       TRIDAG    	  =      TRIDAG%SIZE    K	     a   TRIDAG%A    Ũ	     a   TRIDAG%B    c
     a   TRIDAG%C    ï
     a   TRIDAG%R    {     a   TRIDAG%U             SPLINE_ELEGANT $     =      SPLINE_ELEGANT%SIZE !   Í     a   SPLINE_ELEGANT%X !   Y     a   SPLINE_ELEGANT%Y #   å  @   a   SPLINE_ELEGANT%YP1 #   %  @   a   SPLINE_ELEGANT%YPN "   e     a   SPLINE_ELEGANT%Y2    ņ  Ą       SPLINT      <      SPLINT%MIN    Î  <      SPLINT%MAX    
  =      SPLINT%SIZE    G     a   SPLINT%XA    Ó     a   SPLINT%YA    _     a   SPLINT%Y2A    ë  @   a   SPLINT%X    +  ģ       SPLINT_DERIV !   Þ  <      SPLINT_DERIV%MIN !     <      SPLINT_DERIV%MAX "   V  =      SPLINT_DERIV%SIZE          a   SPLINT_DERIV%XA          a   SPLINT_DERIV%YA !   Ŧ     a   SPLINT_DERIV%Y2A    7  @   a   SPLINT_DERIV%X '   w         SPLINT_DERIV_ALL_NODES ,     =      SPLINT_DERIV_ALL_NODES%SIZE *   A     a   SPLINT_DERIV_ALL_NODES%XA *   Í     a   SPLINT_DERIV_ALL_NODES%YA +   Y     a   SPLINT_DERIV_ALL_NODES%Y2A -   å     a   SPLINT_DERIV_ALL_NODES%DERIV    q        SMOOTH_SPLINE *     D      SMOOTH_SPLINE%DOT_PRODUCT "   Ë  <      SMOOTH_SPLINE%EXP &     @      SMOOTH_SPLINE%PRESENT #   G  =      SMOOTH_SPLINE%TRIM #     =      SMOOTH_SPLINE%SIZE %   Á  L   a   SMOOTH_SPLINE%WEIGHT $     @   a   SMOOTH_SPLINE%ALPHA     M     a   SMOOTH_SPLINE%X     Ų     a   SMOOTH_SPLINE%Y "   e  @   a   SMOOTH_SPLINE%YP1 "   Ĩ  @   a   SMOOTH_SPLINE%YPN !   å     a   SMOOTH_SPLINE%Y2 '   q     a   SMOOTH_SPLINE%VARIANCE    ý         QSIMP      <      QSIMP%ABS    Á     a   QSIMP%X_0    Q     a   QSIMP%Y_0    á     a   QSIMP%Y2_0    q   @   a   QSIMP%A    ą   @   a   QSIMP%B    ņ   @   a   QSIMP%S    1!         TRAPZD    Â!  =      TRAPZD%REAL    ĸ!     a   TRAPZD%X_0    "     a   TRAPZD%Y_0    #     a   TRAPZD%Y2_0    Ŋ#  @   a   TRAPZD%A    ï#  @   a   TRAPZD%B    /$  @   a   TRAPZD%S    o$  @   a   TRAPZD%N    Ŋ$  Õ       ZRIDDR    %  =      ZRIDDR%SIGN    Á%  =      ZRIDDR%SQRT    þ%  <      ZRIDDR%ABS    :&  =      ZRIDDR%SIZE    w&     a   ZRIDDR%X_0    '     a   ZRIDDR%Y_0    '     a   ZRIDDR%Y2_0    '(  @   a   ZRIDDR%X1    g(  @   a   ZRIDDR%X2    §(  @   a   ZRIDDR%ZEROPT    į(  @   a   ZRIDDR%XACC 