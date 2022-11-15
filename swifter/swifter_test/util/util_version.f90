!**********************************************************************************************************************************
!
!  Unit Name   : util_version
!  Unit Type   : subroutine
!  Project     : Swifter
!  Package     : util
!  Language    : Fortran 90/95
!
!  Description : Print program version information to terminal
!
!  Input
!    Arguments : none
!    Terminal  : none
!    File      : none
!
!  Output
!    Arguments : none
!    Terminal  : Program version information
!    File      : none
!
!  Invocation  : CALL util_version
!
!  Notes       : Adapted from Hal Levison's Swift routine util_version.f
!
!**********************************************************************************************************************************
SUBROUTINE util_version

! Modules
     USE module_parameters
     USE module_interfaces, EXCEPT_THIS_ONE => util_version
     IMPLICIT NONE

! Executable code

     RETURN

END SUBROUTINE util_version
!**********************************************************************************************************************************
!
!  Author(s)   : David E. Kaufmann
!
!  Revision Control System (RCS) Information
!
!  Source File : $RCSfile$
!  Full Path   : $Source$
!  Revision    : $Revision$
!  Date        : $Date$
!  Programmer  : $Author$
!  Locked By   : $Locker$
!  State       : $State$
!
!  Modification History:
!
!  $Log$
!**********************************************************************************************************************************
